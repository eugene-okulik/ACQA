words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def key_printer(my_dict):
    for key, value in my_dict.items():
        print(key * value)


key_printer(words)
