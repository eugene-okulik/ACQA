list_with_results = [
    'результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2'
]
add_to_result = 10


def increase_result(text, plus_value):
    value_from_text = int(text.split()[-1])
    return value_from_text + plus_value


for result in list_with_results:
    print(increase_result(result, add_to_result))
