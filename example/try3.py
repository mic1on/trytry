from trytry import trytry


@trytry
def my_function():
    print(1 / 0)


@trytry
def my_function2():
    print(1 / 0)


@my_function.exception(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))


@my_function.finally_
def handle_zero_division_error():
    print(my_function.__name__, "finally")


if __name__ == '__main__':
    my_function()
    # my_function2()
