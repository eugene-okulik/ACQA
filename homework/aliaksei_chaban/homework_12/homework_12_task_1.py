class Flowers:
    def __init__(self, name, lifetime, color, cost, stem_length):
        self.name = name
        self.lifetime = lifetime
        self.color = color
        self.cost = cost
        self.stem_length = stem_length


class Roses(Flowers):
    def __init__(self, color, cost, stem_length):
        super().__init__('Rose', 7, color, cost, stem_length)


class Tulips(Flowers):
    def __init__(self, color, cost, stem_length):
        super().__init__('Tulip', 5, color, cost, stem_length)


class Lilies(Flowers):
    def __init__(self, color, cost, stem_length):
        super().__init__('Lily', 10, color, cost, stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def get_average_lifetime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return round(total_lifetime / len(self.flowers), 1)

    def sort_flowers(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_flower_by_lifetime(self, lifetime_threshold):

        appropriate_flowers_list = [flower.name for flower in self.flowers if flower.lifetime >= lifetime_threshold]

        if appropriate_flowers_list:
            print(f'Cписок цветов, которые простоят {lifetime_threshold} дней или дольше: {appropriate_flowers_list}')
        else:
            print(f'Цветов, которые простоят {lifetime_threshold} дней в букете нет')


rose = Roses('red', 10, 50)
tulip = Tulips('yellow', 7, 30)
lily = Lilies('white', 15, 60)

my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(tulip)
my_bouquet.add_flower(lily)

print(f'Стоимость букета: {my_bouquet.get_cost()}$')
print(f'Средняя продолжительность жизни букета: {my_bouquet.get_average_lifetime()} дней')

my_bouquet.sort_flowers('cost')
print('Цветы отсортированы по цене:', [(flower.name, flower.cost) for flower in my_bouquet.flowers])

my_bouquet.sort_flowers('color')
print('Цветы отсортированы по цвету:', [(flower.name, flower.color) for flower in my_bouquet.flowers])

my_bouquet.sort_flowers('stem_length')
print('Цветы отсортированы по длинне стебля:', [(flower.name, flower.stem_length) for flower in my_bouquet.flowers])

my_bouquet.find_flower_by_lifetime(6)
