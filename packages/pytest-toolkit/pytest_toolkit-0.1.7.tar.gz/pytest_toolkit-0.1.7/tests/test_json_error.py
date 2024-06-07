import importlib

import pytest
from deepdiff.helper import CannotCompare

from pytest_toolkit import get_diff
from pytest_toolkit.errors import FileDoesNotExist


def test_file_not_exist(caplog):
    """
    Названия файла нет, json нет
    """
    with pytest.raises(FileDoesNotExist):
        get_diff(result_dict=None)

    assert (
        "Файл file_not_exist.json не был найден в директории tests/static"
        in caplog.text
    )


def test_filename_not_exist(caplog):
    """
    Название файла есть, json нет
    """
    with pytest.raises(FileDoesNotExist):
        get_diff(result_dict=None, filename="not_exist.json")

    assert "Файл not_exist.json не был найден в директории tests/static" in caplog.text


def test_no_compare():
    with pytest.raises(CannotCompare):
        assert get_diff(result_dict={"example13": "example13"}) == {}


def test_no_compare_deeper():
    with pytest.raises(CannotCompare):
        assert get_diff(result_dict={"example14": {"example14": ["example14"]}}) == {}


def test_no_gitignore(caplog):
    import os

    from pytest_toolkit import configure

    old_filename = ".testignore"
    new_filename = ".testignore2"

    os.rename(old_filename, new_filename)
    importlib.reload(configure)
    os.rename(new_filename, old_filename)

    assert "Файл .testignore не найден" in caplog.text
