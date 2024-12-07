import mysql.connector as mysql

db = mysql.connect(
    username="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    db="st-onl"
)

cursor = db.cursor(dictionary=True)


def insert_and_get_id(cursor, table_name, columns, values):
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['%s'] * len(columns))
    query = f'INSERT INTO `{table_name}` ({columns_str}) VALUES ({placeholders})'
    cursor.execute(query, values)

    return cursor.lastrowid


# Создание студента
students_table_columns = ['name', 'second_name', 'group_id']
student_info = ('Aliaksei', 'Chaban', None)

new_student_id = insert_and_get_id(cursor, 'students', students_table_columns, student_info)

# Создание книг и добавление их студенту
books_table_columns = ['title', 'taken_by_student_id']

first_book_info = ('How to become a AQA', new_student_id)
second_book_info = ('CI and CD', new_student_id)
third_book_info = ('What is Kanban', new_student_id)

first_book_id = insert_and_get_id(cursor, 'books', books_table_columns, first_book_info)
second_book_id = insert_and_get_id(cursor, 'books', books_table_columns, second_book_info)
third_book_id = insert_and_get_id(cursor, 'books', books_table_columns, third_book_info)

# Создание новой группы
groups_table_columns = ['title', 'start_date', 'end_date']
new_group_info = ('Software tester', 'nov 2024', 'feb 2023')

new_group_id = insert_and_get_id(cursor, 'groups', groups_table_columns, new_group_info)

# Привязка нового студента к новой группе
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s;", (new_group_id, new_student_id))

# Создание предметов
subjets_table_columns = ['title']

first_subj_id = insert_and_get_id(cursor, 'subjets', subjets_table_columns, ('Python core',))
second_subj_id = insert_and_get_id(cursor, 'subjets', subjets_table_columns, ('Functional testing',))

# Создание уроков для предметов
lessons_table_columns = ['title', 'subject_id']

first_lesson_first_subj = ('Lesson-1', first_subj_id)
second_lesson_first_subj = ('Lesson-2', first_subj_id)
first_lesson_second_subj = ('Lesson-1', second_subj_id)
second_lesson_second_subj = ('Lesson-2', second_subj_id)

l1_s1_id = insert_and_get_id(cursor, 'lessons', lessons_table_columns, first_lesson_first_subj)
l2_s1_id = insert_and_get_id(cursor, 'lessons', lessons_table_columns, second_lesson_first_subj)
l1_s2_id = insert_and_get_id(cursor, 'lessons', lessons_table_columns, first_lesson_second_subj)
l2_s2_id = insert_and_get_id(cursor, 'lessons', lessons_table_columns, second_lesson_second_subj)

# Добавление оценок за уроки
marks_table_columns = ['value', 'lesson_id', 'student_id']
mark_l1_s1_info = (10, l1_s1_id, new_student_id)
mark_l2_s1_info = (9, l2_s1_id, new_student_id)
mark_l1_s2_info = (8, l1_s2_id, new_student_id)
mark_l2_s2_info = (7, l2_s2_id, new_student_id)

mark_l1_s1_id = insert_and_get_id(cursor, 'marks', marks_table_columns, mark_l1_s1_info)
mark_l2_s1_id = insert_and_get_id(cursor, 'marks', marks_table_columns, mark_l2_s1_info)
mark_l1_s2_id = insert_and_get_id(cursor, 'marks', marks_table_columns, mark_l1_s2_info)
mark_l2_s2_id = insert_and_get_id(cursor, 'marks', marks_table_columns, mark_l2_s2_info)

# Все оценки студента
cursor.execute('SELECT value FROM marks WHERE student_id = %s', (new_student_id,))

marks = cursor.fetchall()
print("Оценки студента:", marks)

# Все книги, которые находятся у студента
cursor.execute('SELECT title FROM books WHERE taken_by_student_id = %s', (new_student_id,))

books = cursor.fetchall()
print("Книги студента:", books)

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
cursor.execute(
    '''SELECT *
    FROM students
    JOIN books ON students.id = books.taken_by_student_id
    JOIN `groups` g ON students.group_id = g.id
    JOIN marks ON students.id = marks.student_id
    WHERE students.id = %s;
    ''', (new_student_id,)
)

result = cursor.fetchall()
print("Подробная информация о студенте:")
for row in result:
    print(row)

db.commit()
db.close()
