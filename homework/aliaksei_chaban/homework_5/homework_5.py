# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Задание 2

first_result = 'результат операции: 42'
second_result = 'результат операции: 514'
third_result = 'результат работы программы: 9'
add_to_result = 10

def increase_result(text, plus_value):
    text_semicolon_index = text.index(':')
    value_index = text_semicolon_index + 2
    extracted_value = int(text[value_index:])
    return extracted_value + plus_value


print(increase_result(first_result, add_to_result))
print(increase_result(second_result, add_to_result))
print(increase_result(third_result, add_to_result))

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_to_string = ', '.join(students)
subjects_to_string = ', '.join(subjects)

print(f'Students {students_to_string} study these subjects: {subjects_to_string}')
