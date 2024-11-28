class Book:

    page_material = 'Бумага'
    is_text_present = True


    def __init__(self, book_name, author, pages_count, isbn, is_taken=False):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.is_taken = is_taken


    def book_info(self):
        if not self.is_taken:
            print(
                f'Название: {self.book_name}, '
                f'Автор: {self.author}, '
                f'страниц: {self.pages_count}, '
                f'материал: {self.page_material}'
            )
        else:
            print(
                f'Название: {self.book_name}, '
                f'Автор: {self.author}, '
                f'страниц: {self.pages_count}, '
                f'материал: {self.page_material}, '
                f'зарезервирована'
            )


class Textbook(Book):

    def __init__(self, book_name, author, pages_count, isbn, subject, school_class, homework, is_taken=False):
        super().__init__(book_name, author, pages_count, isbn, is_taken)
        self.subject = subject
        self.school_class = school_class
        self.homework = homework


    def book_info(self):
        if not self.is_taken:
            print(
                f'Название: {self.book_name}, '
                f'Автор: {self.author}, '
                f'страниц: {self.pages_count}, '
                f'предмет: {self.subject}, '
                f'класс: {self.school_class}'
            )
        else:
            print(
                f'Название: {self.book_name}, '
                f'Автор: {self.author}, '
                f'страниц: {self.pages_count}, '
                f'предмет: {self.subject}, '
                f'класс: {self.school_class}, '
                f'зарезервирована'
            )


first_book = Book(
    'Пролетая над гнездом кукушки', 'Кен Кизи', 320, '978-5-17-070621-0'
)

second_book = Book(
    'Цветы для Элджернона', 'Дэниел Киз', 384, '978-5-17-083530-9'
)

third_book = Book(
    'Триумфальная арка', 'Эрих Мария Ремарк', 448, '978-5-17-084123-2'
)

fourth_book = Book(
    'Удивительная история Билли Миллигана', 'Дэниел Киз', 528, '978-5-17-085123-1'
)

fifth_book = Book(
    'Вино из одуванчиков', 'Рэй Брэдбери', 256, '978-5-17-086124-7', True
)

math_textbook = Textbook(
    'Математика для начальных классов', 'Петр Петров', 300, '333-33-3',
    'Математика', 1, True
)

english_textbook = Textbook(
    'Английский для начальных классов', 'Иван Иванов', 400, '222-22-2',
    'Английский язык', 4, False
)

computer_science_textbook = Textbook(
    'Основы дата анализа', 'Джон Уайт', 600, '111-11-1', 'Информатика',
    11, True, True
)


list_of_books = [first_book, second_book, third_book, fourth_book, fifth_book]
list_of_textbooks = [math_textbook, english_textbook, computer_science_textbook]


def list_printer(some_list):
    for some_book in some_list:
        some_book.book_info()


list_printer(list_of_books)
print('-' * 150)
list_printer(list_of_textbooks)
