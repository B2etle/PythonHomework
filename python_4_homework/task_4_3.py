import os
from csv import DictReader, DictWriter
from pathlib import Path
from typing import List


def get_top_performers(file_path: str, number_of_top_students: int = 5) -> List[str]:
    """Return names of top performer students."""
    with open(file_path, 'r', newline='') as file_students:
        students_reader = DictReader(file_students, delimiter=',')
        students = sorted(students_reader, key=lambda student: (float(student['average mark'])), reverse=True)
        return [student['student name'] for student in students[:number_of_top_students]]


def order_students_by_age(file_path: str):
    """Write CSV student information to the file in descending order of age."""
    with open(file_path, 'r', newline='') as read_students:
        students_reader = DictReader(read_students, delimiter=',')
        students = sorted(students_reader, key=lambda student: (int(student['age'])), reverse=True)
    file_name = f'{os.path.dirname(file_path)}/{Path(file_path).resolve().stem}'
    with open(f'{file_name}_order_by_age.csv', 'w', newline='') as write_students:
        students_writer = DictWriter(write_students, students_reader.fieldnames)
        students_writer.writeheader()
        students_writer.writerows(students)

order_students_by_age('/home/tamara/Documents/WorkSpace/Trainings/Introduction_to_Python/Python/PythonHomework/python_4_homework/students.csv')
