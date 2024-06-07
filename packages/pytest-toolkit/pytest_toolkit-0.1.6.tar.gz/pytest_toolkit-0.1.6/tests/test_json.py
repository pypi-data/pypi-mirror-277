from pytest_toolkit import get_diff, get_file_json


def test_correct_comparasion_diff():
    """
    Название файла есть, поэтому ищем файл по названию. Такой файл один.
    """
    assert (
        get_diff(
            result_dict={"example1": "example1"}, filename="correct_comparasion_diff.json"
        )
        == {}
    )


def test_filename_search_diff():
    """
    Названия файла нет, поэтому ищем файл по названию функции.
    Таких файлов несколько, поэтому выбираем тот, который лежит
    в директории json
    """
    assert get_diff(result_dict={"example2": "example2"}) == {}


def test_correct_comparasion_file():
    """
    Название файла есть, поэтому ищем файл по названию. Такой файл один.
    """
    assert get_file_json(filename="correct_comparasion_diff.json") == {"example1": "example1"}


def test_filename_search_file():
    """
    Названия файла нет, поэтому ищем файл по названию функции.
    Таких файлов несколько, поэтому выбираем тот, который лежит
    в директории json
    """
    assert get_file_json() == {"example2": "example2"}
