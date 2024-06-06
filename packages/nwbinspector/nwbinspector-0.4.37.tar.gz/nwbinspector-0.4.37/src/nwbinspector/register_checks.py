"""Primary decorator used on a check function to add it to the registry and automatically parse its output."""

from collections.abc import Iterable
from functools import wraps
from enum import Enum
from dataclasses import dataclass
from typing import Optional

import h5py
from pynwb import NWBFile
from pynwb.file import Subject
from pynwb.ecephys import Device, ElectrodeGroup


class Importance(Enum):
    """A definition of the valid importance levels for a given check function."""

    ERROR = 4
    PYNWB_VALIDATION = 3
    CRITICAL = 2
    BEST_PRACTICE_VIOLATION = 1
    BEST_PRACTICE_SUGGESTION = 0


class Severity(Enum):
    """
    A definition of the valid severity levels for the output from a given check function.

    Strictly for internal development that improves report organization; users should never directly see these values.
    """

    HIGH = 2
    LOW = 1


available_checks = list()


@dataclass
class InspectorMessage:
    """
    The primary output to be returned by every check function.

    Parameters
    ----------
    message : str
        A message that informs the user of the violation.
    severity : Severity, optional
        If a check of non-CRITICAL importance has some basis of comparison, such as magnitude of affected data, then
        the developer of the check may set the severity as Severity.HIGH or Severity.LOW by calling
        `from nwbinspector.register_checks import Severity`. A good example is comparing if h5py.Dataset compression
        has been enabled on smaller vs. larger objects (see nwbinspector/checks/nwb_containers.py for details).

        The user will never directly see this severity, but it will prioritize the order in which check results are
        presented by the NWBInspector.

    importance : Importance
        The Importance level specified by the decorator of the check function.
    check_function_name : str
        The name of the check function the decorator was applied to.
    object_type : str
        The specific class of the instantiated object being inspected.
    object_name : str
        The name of the instantiated object being inspected.
    location : str
        The location relative to the root of the NWBFile where the inspected object may be found.
    file_path : str
        The path of the NWBFile this message pertains to
        Relative to the path called from inspect_nwb, inspect_all, or the path specified at the command line.
    """

    message: str
    importance: Importance = Importance.BEST_PRACTICE_SUGGESTION
    severity: Severity = Severity.LOW
    check_function_name: str = None
    object_type: str = None
    object_name: str = None
    location: Optional[str] = None
    file_path: str = None

    def __repr__(self):
        """Representation for InspectorMessage objects according to black format."""
        return "InspectorMessage(\n" + ",\n".join([f"    {k}={v.__repr__()}" for k, v in self.__dict__.items()]) + "\n)"


# TODO: neurodata_type could have annotation hdmf.utils.ExtenderMeta, which seems to apply to all currently checked
# objects. We can wait and see how well that holds up before adding it in officially.
def register_check(importance: Importance, neurodata_type):
    """
    Wrap a check function with this decorator to add it to the check registry and automatically parse some output.

    Parameters
    ----------
    importance : Importance
        Importance has three levels:
            CRITICAL
                - potentially incorrect data
            BEST_PRACTICE_VIOLATION
                - very suboptimal data representation
            BEST_PRACTICE_SUGGESTION
                - improvable data representation
    neurodata_type
        The most generic HDMF/PyNWB class the check function applies to.
        Should generally match the type annotation of the check.
        If this check is intended to apply to any general NWBFile object, set neurodata_type to None.
    """

    def register_check_and_auto_parse(check_function):
        if importance not in [
            Importance.CRITICAL,
            Importance.BEST_PRACTICE_VIOLATION,
            Importance.BEST_PRACTICE_SUGGESTION,
        ]:
            raise ValueError(
                f"Indicated importance ({importance}) of custom check ({check_function.__name__}) is not a valid "
                "importance level! Please choose one of Importance.CRITICAL, Importance.BEST_PRACTICE_VIOLATION, "
                "or Importance.BEST_PRACTICE_SUGGESTION."
            )
        check_function.importance = importance
        check_function.neurodata_type = neurodata_type

        @wraps(check_function)
        def auto_parse_some_output(*args, **kwargs) -> InspectorMessage:
            if args:
                obj = args[0]
            else:
                obj = kwargs[list(kwargs)[0]]
            output = check_function(*args, **kwargs)
            auto_parsed_result = None
            if isinstance(output, InspectorMessage):
                auto_parsed_result = auto_parse(check_function=check_function, obj=obj, result=output)
            elif output is not None:
                auto_parsed_result = list()
                for result in output:
                    auto_parsed_result.append(auto_parse(check_function=check_function, obj=obj, result=result))
                if not any(auto_parsed_result):
                    auto_parsed_result = None
            return auto_parsed_result

        available_checks.append(auto_parse_some_output)

        return auto_parse_some_output

    return register_check_and_auto_parse


def auto_parse(check_function, obj, result: Optional[InspectorMessage] = None):
    """Automatically fill values in the InspectorMessage from the check function."""
    if result is not None:
        auto_parsed_result = result
        if not isinstance(auto_parsed_result.severity, Severity):
            raise ValueError(
                f"Indicated severity ({auto_parsed_result.severity}) of custom check "
                f"({check_function.__name__}) is not a valid severity level! Please choose one of "
                "Severity.HIGH, Severity.LOW, or do not specify any severity."
            )
        auto_parsed_result.importance = check_function.importance
        auto_parsed_result.check_function_name = check_function.__name__
        auto_parsed_result.object_type = type(obj).__name__
        auto_parsed_result.object_name = obj.name
        auto_parsed_result.location = parse_location(neurodata_object=obj)
        return auto_parsed_result


def parse_location(neurodata_object) -> Optional[str]:
    """Grab the object location from a h5py.Dataset or a container content that is an h5py.Dataset object."""
    known_locations = {
        NWBFile: "/",
        Subject: "/general/subject",
        Device: f"/general/devices/{neurodata_object.name}",
        ElectrodeGroup: f"/general/extracellular_ephys/{neurodata_object.name}",
        # TODO: add ophys equivalents
    }

    for key, val in known_locations.items():
        if isinstance(neurodata_object, key):
            return val
    """Infer the human-readable path of the object within an NWBFile by tracing its parents."""
    if neurodata_object.parent is None:
        return "/"
    # Best solution: object is or has a HDF5 Dataset
    if isinstance(neurodata_object, h5py.Dataset):
        return neurodata_object.name
    else:
        for field in neurodata_object.fields.values():
            if isinstance(field, h5py.Dataset):
                return field.parent.name
