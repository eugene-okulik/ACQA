text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' +
        ' dignissim vitae libero')
words = text.split()
modified_words = []

for word in words:
    if word.endswith(','):
        word = word[:-1] + 'ing' + ','
    elif word.endswith('.'):
        word = word[:-1] + 'ing' + '.'
    else:
        word += 'ing'
    modified_words.append(word)

modified_text = ' '.join(modified_words)
print(modified_text)
