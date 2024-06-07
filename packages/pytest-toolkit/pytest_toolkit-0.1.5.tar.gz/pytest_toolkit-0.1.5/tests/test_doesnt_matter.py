from pytest_toolkit import get_diff


def test_default():
    assert get_diff(result_dict={"example4": "example4"}) == {}


def test_equals():
    assert get_diff(result_dict={"example5": "example5"}) == {}


def test_gt():
    assert get_diff(result_dict={"example6": 8}) == {}
