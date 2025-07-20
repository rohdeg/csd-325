""" student_json_practice.py by Garrett Rohde
    07/20/2025
    Assignment 8.2
    Reading and appending to .json files
"""

import json
import sys

def load_students(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
    except json.decoder.JSONDecodeError:
        print(f"Error: File {file} could not be decoded.")


def print_students(students, title):
    print(f"\n{title}:")
    for student in students:
        full_name = f"{student.get('L_Name', 'N/A')}, {student.get('F_Name', 'N/A')}"
        student_id = f"{student.get('Student_ID', 'N/A')}"
        student_email = f"{student.get('Email', 'N/A')}"
        print(f"{full_name} : ID = {student_id}, Email = {student_email}")


def add_student(students, new_student):
    # only add the new student if they are not currently in the list
    if new_student not in students:
        students.append(new_student)
        print("\nNew student added.")
        with open("student.json", "w") as f:
            json.dump(students, f, indent=4)    # pretty formatting


def main():
    students = load_students("student.json")
    print_students(students, "Original List")

    # create a new student dict to append to list
    new_student = {
        "L_Name": "Rohde",
        "F_Name": "Garrett",
        "Student_ID": 26111,
        "Email": "grohde@bellevue.edu",
    }
    add_student(students, new_student)

    print_students(students, "Updated List")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # exit when ctrl-c is pressed