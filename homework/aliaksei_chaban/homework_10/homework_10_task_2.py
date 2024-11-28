# Вариант 1
def my_first_decorator(func):

    def wrapper(*args, count=1, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@my_first_decorator
def func_with_decorator(text):
    print(text)


func_with_decorator('Выполнение функции ...', count=2)


# Вариант 2
def repeat_me(count=1):

    def my_second_decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper
    return my_second_decorator


@repeat_me(count=3)
def some_func(text):
    print(text)


some_func('Repeat me ...')
