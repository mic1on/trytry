# TryTry
<a href="https://pypi.org/project/trytry" target="_blank">
    <img src="https://img.shields.io/pypi/v/trytry.svg" alt="Package version">
</a>

<a href="https://pypi.org/project/trytry" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/trytry.svg" alt="Supported Python versions">
</a>

[中文文档](README_ZH.md)


## install

```bash
pip install trytry
```

## Example

### handle exception

```python
from trytry import trytry


@trytry
def my_function():
    raise FileNotFoundError('file not found')


@trytry
def my_function2():
    print(1 / 0)


@trytry.exception(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))


@trytry.exception(FileNotFoundError)
def handle_file_not_found_error(func, e):
    print(func.__name__, str(e))


if __name__ == '__main__':
    my_function()
    my_function2()
```


### handle all exception

```python
from trytry import trytry


@trytry
def my_function():
    raise FileNotFoundError('file not found')


@trytry
def my_function2():
    print(1 / 0)


@trytry.exception(Exception)
def handle_all_error(func, e):
    print(func.__name__, str(e))


if __name__ == '__main__':
    my_function()
    my_function2()
```

All of the above exceptions are caught and are global exceptions. 
You can also catch exceptions for specific functions.
```python
from trytry import trytry


@trytry
def my_function():
    print(1 / 0)

@my_function.exception(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))
```
