# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел


def arithmetic_mean(a, b):
    return (a + b) / 2


def geometric_mean(a, b):
    return (a * b) ** 0.5


first_value = 10
second_value = 5

print(arithmetic_mean(first_value, second_value))
print(geometric_mean(first_value, second_value))
