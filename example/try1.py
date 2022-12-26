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


@my_function.finally_
def my_function_finally():
    print(my_function.__name__, "finally")


if __name__ == '__main__':
    my_function()
    my_function2()
