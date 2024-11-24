mystery_number = 33
is_guessed = False

print('-' * 60)
print('Игра "Угадайка", попробуй раскрыть тайну мистического числа')
print('-' * 60)

while not is_guessed:
    user_guess = int(input('Твой вариант ---> '))
    if user_guess == mystery_number:
        print('Поздравляю! Вы угадали!')
        is_guessed = True
    else:
        print('Нет, это не оно. Попробуйте снова')
