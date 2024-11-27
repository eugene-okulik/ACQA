def decorator(func):

    def wrapper(f_num, s_num):

        if f_num == s_num:
            operation = '+'
        elif f_num > s_num:
            operation = '-'
        elif f_num < s_num:
            operation = '/'
        elif f_num < 0 or s_num < 0:
            operation = '*'

        return func(f_num, s_num, operation)
    return wrapper


@decorator
def calc(first, second, operation):

    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return 'Error: Division by zero'
    elif operation == '*':
        return first * second

first_value = int(input('Введите первое целое число: '))
second_value = int(input('Введите второе целое число: '))

print(calc(first_value, second_value))
