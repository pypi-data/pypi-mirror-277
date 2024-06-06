
A powerful tool that allows you to add custom attributes and variables to your tests. 

With this plugin, you can easily attach additional data to each test, which can then be referenced by fixtures or even the test itself.
This enables you to create more flexible and dynamic test suites tailored to your specific needs.


Features
--------

- Custom Attributes for Tests: Add custom attributes to individual tests using the @attributes marker, allowing you to store important metadata or configuration data directly with the test.

- Access Attributes in Fixtures: Easily access attribute values within fixtures, enabling you to create dynamic fixtures that adapt to the specific requirements of each test.

- Reference Attributes in Tests: Directly access attribute values within the test functions themselves, providing a convenient way to parameterize tests, perform conditional logic, or customize test behavior based on the attached attributes.


Installation
------------

```bash
pip install pytest-attributes
```


Usage
-----

First, import attributes from pytest_attributes:

```python
from pytest_attributes import attributes
```


Now you can add attributes to each of your tests using the @attributes marker. Like so:

```python
@attributes(
    step = 1,
    action = "Test the functionality of feature X",
    expected = "Feature X works successfully"
    )
def test_functionality():
    assert True
```

In the above example, we created our attributes marker, and then added whatever parameters we wanted inside and set those values.
Now those values are associated with this specific test called "test_functionality".


We can now reference these attributes by using the provided keyterm 'attr':

```python
@attributes(
    step = 1,
    action = "Test the functionality of feature X",
    expected = "Feature X works successfully"
    )
def test_functionality(attr):
    print(attr.step)
    print(attr.action)
    print(attr.expected)
    assert True
```

The above example prints the following:

```bash
test.py 1
Test the functionality of feature X
Feature X works successfully
.
```


More importantly, however, we can use attr to get these attributes from within fixtures!
This opens up the door to many possibilities, such as determining what to do with each test before running it, attaching attributes to report files, and even sending them alongside the test results to any desired endpoints. 

The process of doing this is extremely simple.
Simply provide attr as an argument to the desired fixture and you can access its attributes. Like so:

```python
@pytest.fixture(autouse=True)
def my_fixture(attr):
    print(attr.action)
```


Example Code
------------

my_test.py

```python
import pytest
from pytest_attributes import attributes

@attributes(
    step = 1,
    action = "Test the functionality of feature X",
    expected = "Feature X works successfully"
    )
def test_functionality(attr):
    print(attr.step)
    print(attr.action)
    print(attr.expected)
    assert True
```


conftest.py

```python
import pytest

@pytest.fixture(autouse=True)
def my_fixture(attr):
    print(attr.action)
```


Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.


License
-------

Distributed under the terms of the `BSD-3`_ license, "pytest-attributes" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/MichaelE55/pytest-attributes/issues
