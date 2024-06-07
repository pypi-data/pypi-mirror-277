from pytest_toolkit import get_diff


def test_dict_remove():
    assert get_diff(result_dict={"example7": "example7"}) == {
        "Элемент словаря убран": ["root['remove']"]
    }


def test_dict_add():
    assert get_diff(result_dict={"example8": "example8", "add": "add"}) == {
        "Элемент словаря добавлен": ["root['add']"]
    }


def test_iterable_remove():
    assert get_diff(result_dict={"example9": ["example9"]}) == {
        "Элемент списка убран": {"root['example9'][1]": "remove"}
    }


def test_iterable_add():
    assert get_diff(result_dict={"example10": ["example10", "add"]}) == {
        "Элемент списка добавлен": {"root['example10'][1]": "add"}
    }


def test_change_type():
    assert get_diff(result_dict={"example11": 11}) == {
        "Значение или тип элемента изменены": {
            "root['example11']": {
                "new_type": int,
                "new_value": 11,
                "old_type": str,
                "old_value": "11",
            }
        }
    }


def test_change_value():
    assert get_diff(result_dict={"example12": 13}) == {
        "Значение или тип элемента изменены": {
            "root['example12']": {
                "new_value": 13,
                "old_value": 12,
            }
        }
    }
