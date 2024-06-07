from pytest_toolkit import get_diff


def test_filename_search():
    """
    Названия файла нет, поэтому ищем файл по названию функции.
    Таких файлов несколько. Тк ни один из них не лежит в директории
    json_default, то выбираем стандартную директорию default
    """
    assert get_diff(result_dict={"example3": "example3"}) == {}
