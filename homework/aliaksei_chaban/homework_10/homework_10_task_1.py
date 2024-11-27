def my_first_decorator(func):

    def wrapper(*args, **kwargs):
        print()
        func(*args, **kwargs)
        print()
        print('finished')

    return wrapper


@my_first_decorator
def func_with_decorator(text):
    print(text)

my_text = 'Выполнение функции ...'
func_with_decorator(my_text)
