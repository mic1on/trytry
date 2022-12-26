# TryTry


## 安装

```bash
pip install trytry
```

## 案例

### 捕获指定异常

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


### 捕获所有异常

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
以上所有异常都会被捕获，属于全局异常，你也可以对特定函数进行异常捕获。
```python
from trytry import trytry


@trytry
def my_function():
    print(1 / 0)

@my_function.exception(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))
```
