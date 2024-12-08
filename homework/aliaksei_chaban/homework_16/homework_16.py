import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    username=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    db=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    '''
    SELECT
        students.name,
        students.second_name,
        g.title AS group_title,
        COALESCE(books.title, '') AS book_title,
        COALESCE(subjets.title, '') AS subject_title,
        COALESCE(lessons.title, '') AS lesson_title,
        COALESCE(marks.value, '') AS mark_value
    FROM students
    LEFT JOIN `groups` g ON students.group_id = g.id
    LEFT JOIN books ON students.id = books.taken_by_student_id
    LEFT JOIN marks ON students.id = marks.student_id
    LEFT JOIN lessons ON marks.lesson_id = lessons.id
    LEFT JOIN subjets ON lessons.subject_id = subjets.id;
    '''
)

data_from_db = cursor.fetchall()
db.close()

homework_16_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
mentors_file_path = os.path.join(homework_16_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(mentors_file_path, newline='') as csv_file:
    data_from_csv = [row for row in csv.DictReader(csv_file)]

values_from_db = [tuple(d.values()) for d in data_from_db]
values_from_csv = [tuple(d.values()) for d in data_from_csv]
missing_data = [item for item in values_from_csv if item not in values_from_db]

for row in missing_data:
    print(row)
