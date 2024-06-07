# pytest_toolkit

pytest_toolkit - is an useful utils for testing applications

# how to use

1. Installation
    ```
    pip install pytest-toolkit
    ```
    ```
    pytest tests/
    ```
2. Get started 
    ```
    The advantage is in having clear understanding of difference between 
    response.json and static json. For example
    {
        'Значение или тип элемента изменены': 
        {"root['example1']": {'new_value': 'example2', 'old_value': 'example1'}}
    } == {}
    Its easy to see that value of key 'example1' changed from 'example1' to 'example2'.
    ```
    ```
    from pytest_toolkit import get_diff

    def test():
        response = client.get(url)
        assert get_diff(result_dict=response.json()) == {}
    ```
    OR
    ```
    from pytest_toolkit import get_file_json

    def test():
        response = client.get(url)
        assert get_file_json() == response.json()
    ```
3. Static files search
    ```
    1. You need to create static directory in tests/
    2. If you create filename test_a.py with test_b function, you need to 
    create "a" directory in static directory and "b.json" in directory "a". 
    Library will automatically find a file for get_diff function
    3. If you don't have directory "a" in static files, library will try
    to find file "b.json" in "default" directory first

    If you don't want compare responses manually, you can use get_file_json function:
    ```
    ```
    from pytest_toolkit import get_file_json

    def test():
        response = client.get(url)
        assert get_file_json() == {"test": "test"}
    ```
4. DOESNT_MATTER
    ```
    1. If you don't care about value of dictionary, but you need a key, you
    can write "DOESNT_MATTER" in value and library will skip checking of this field.
    2. If you need to have a constraint for value, you can write python code,
    for example "DOESNT_MATTER > 9" and library will check response.json() value is more than 9.
    ```
5. Check directory tests for more information and examples
6. Coverage
    ```
    ---------- coverage: platform darwin, python 3.12.1-final-0 ----------
    Name                          Stmts   Miss  Cover
    -------------------------------------------------
    pytest_toolkit/__init__.py        2      0   100%
    pytest_toolkit/configure.py       9      0   100%
    pytest_toolkit/constants.py       5      0   100%
    pytest_toolkit/errors.py          2      0   100%
    pytest_toolkit/json.py           83      0   100%
    -------------------------------------------------
    TOTAL                           101      0   100%
    ```
