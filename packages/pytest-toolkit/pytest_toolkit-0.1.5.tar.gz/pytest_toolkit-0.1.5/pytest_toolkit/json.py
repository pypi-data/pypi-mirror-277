import inspect
import json
import os
import pathlib
from copy import deepcopy
from typing import Any

import deepdiff
from deepdiff.helper import CannotCompare

from .configure import logger, matches
from .constants import (DICT_ITEM_ADDED, DICT_ITEM_REMOVED,
                        ITERABLE_ITEM_ADDED, ITERABLE_ITEM_REMOVED,
                        VALUES_OR_TYPE)
from .errors import FileDoesNotExist


def _priority_key(
    filename: str | None, caller_name: str, caller_filename: str
) -> callable:
    caller_name += ".json"

    def wrapper(string):
        points = 0
        if filename is not None and string.endswith(filename):
            points += 128
        if string.endswith(caller_name):
            points += 64
        if caller_filename in string[:-5]:
            points += 32
        if "default" in string:
            points += 16
        return points

    return wrapper


def _get_all_files_in_directory(directory: str) -> list[str]:
    all_files = []

    # Рекурсивно обходим все файлы в директории
    for file_path in pathlib.Path(directory).rglob("*.json"):
        if file_path.is_file() and not matches(file_path):
            all_files.append(str(file_path))

    return all_files


def _get_json(
    filename: str | None, caller_name: str, caller_filename: str
) -> dict | list:
    directory_path = os.getcwd()
    files_in_directory = _get_all_files_in_directory(directory_path)

    try:
        full_path = sorted(
            files_in_directory,
            key=_priority_key(filename, caller_name, caller_filename),
            reverse=True,
        )[0]
        if _priority_key(filename, caller_name, caller_filename)(full_path) < 64:
            raise IndexError
    except IndexError:
        logger.error(
            f"Файл {filename or (caller_name + '.json')} не был найден в директории tests/static"
        )
        raise FileDoesNotExist

    with open(full_path) as json_file:
        output = json.load(json_file)

    return output


def _add_diff_extra(
    diff: dict, diff_values_changed: dict, old_key: str | None, new_key: str
):
    if old_key:
        diff_extra = diff.get(old_key)
    else:
        diff_extra = diff
    if diff_extra:
        diff_values_changed[new_key] = diff_extra


def _find_diff(diff: dict) -> dict:
    try:
        diff_output = {}
        diff_change_values_or_type = deepcopy(
            diff.get("values_changed", {}) | diff.get("type_changes", {})
        )
        for k, v in deepcopy(diff_change_values_or_type).items():
            if isinstance(v["old_value"], str) and "DOESNT_MATTER" in v["old_value"]:
                DOESNT_MATTER = v["new_value"]
                if v["old_value"] != "DOESNT_MATTER" and eval(v["old_value"]):
                    del diff_change_values_or_type[k]
            if v["old_value"] == "DOESNT_MATTER":
                del diff_change_values_or_type[k]

        _add_diff_extra(diff_change_values_or_type, diff_output, None, VALUES_OR_TYPE)
        _add_diff_extra(diff, diff_output, "dictionary_item_removed", DICT_ITEM_REMOVED)
        _add_diff_extra(diff, diff_output, "dictionary_item_added", DICT_ITEM_ADDED)
        _add_diff_extra(diff, diff_output, "iterable_item_removed", ITERABLE_ITEM_REMOVED)
        _add_diff_extra(diff, diff_output, "iterable_item_added", ITERABLE_ITEM_ADDED)

        """
        json doesn't have set

        _add_diff_extra(diff, diff_change, "set_item_removed", SET_ITEM_REMOVED)
        _add_diff_extra(diff, diff_change, "set_item_added", SET_ITEM_ADDED)
        """
    
    except Exception:
        raise CannotCompare()

    return diff_output


def _compare_func(x: Any, y: Any, level=None) -> bool:
    try:
        diff = deepdiff.DeepDiff(
            x, y, ignore_string_type_changes=True, iterable_compare_func=_compare_func
        )
        assert _find_diff(diff) == {}
        return True
    except Exception:
        raise CannotCompare()


def get_file_json(*, filename: str | None = None):
    caller_name = inspect.currentframe().f_back.f_code.co_name.replace("test_", "")
    caller_filename = (
        inspect.stack()[1]
        .filename.split(os.path.sep)[-1]
        .replace(".py", "")
        .replace("test_", "")
    )
    return _get_json(filename, caller_name, caller_filename)


def get_diff(*, result_dict: dict, filename: str | None = None) -> bool:
    caller_name = inspect.currentframe().f_back.f_code.co_name.replace("test_", "")
    caller_filename = (
        inspect.stack()[1]
        .filename.split(os.path.sep)[-1]
        .replace(".py", "")
        .replace("test_", "")
    )

    file_dict = _get_json(filename, caller_name, caller_filename)
    diff = deepdiff.DeepDiff(
        file_dict,
        result_dict,
        ignore_string_type_changes=True,
        iterable_compare_func=_compare_func,
    )
    return _find_diff(diff)
