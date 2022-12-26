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
