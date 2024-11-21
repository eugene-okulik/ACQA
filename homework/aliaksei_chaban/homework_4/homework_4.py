my_dict = {
    'tuple':('audi', 'volvo', 'dodge', 'toyota', 'bmw'),
    'list':['one', 'two', 'three', 'four', 'five'],
    'dict':{'box1': 20, 'box2': 5, 'box3': 3, 'box4': 66, 'box5': 97},
    'set':{1,2,3,4,5}
}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
print(my_dict['tuple'][-1])

#Для того, что хранится под ключом ‘list’:добавьте в конец списка еще один элемент, удалите второй элемент списка
my_dict['list'].append('six')
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict']['i am a tuple'] = 'test'
my_dict['dict'].pop('box1')

#Для того, что хранится под ключом ‘set’:добавьте новый элемент в множество, удалите элемент из множества
my_dict['set'].add(6)
my_dict['set'].remove(3)

print(my_dict)
