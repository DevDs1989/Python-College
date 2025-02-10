from typing import List


def add_student(student_info: dict, sap_id: int, name: str, subjects: List[int]):
    if sap_id in student_info:
        print("Student already exists")
        return
    student_info[sap_id] = {
        "name": name,
        "marks": {"maths": subjects[0], "python": subjects[1], "dsa": subjects[2]},
    }


def total_average(student_info: dict) -> int:
    total = 0
    for sap_id in student_info:
        total += student_average(student_info, sap_id)
    return int(total / len(student_info))


def student_average(student_info: dict, sap_id: int) -> int:
    student = student_info[sap_id]
    marks = student["marks"]
    return int(sum(marks.values()) / len(marks))


def percent_passed(student_info: dict) -> int:
    count = 0
    for sap_id in student_info:
        if student_average(student_info, sap_id) > 33:
            count += 1
    return int(count / len(student_info) * 100)


def percent_failed(student_info: dict) -> int:
    count = 0
    for sap_id in student_info:
        if student_average(student_info, sap_id) <= 33:
            count += 1
    return int(count / len(student_info) * 100)


def student_pass(student_info: dict, sap_id: int) -> bool:
    return student_average(student_info, sap_id) > 33


def print_student_info(student_info: dict):
    sap_id = int(input("Enter SAP ID: "))
    student = student_info.get(sap_id)
    if student:
        print(f"Name: {student['name']}")
        print("Marks".center(20, "-"))
        for subject, marks in student["marks"].items():
            print(f"{subject}: {marks}")
    else:
        print("Student not found")


def average_per_subject(student_info: dict) -> dict:
    subjects = {"Maths": 0, "Python": 0, "DSA": 0}
    for sap_id in student_info:
        student = student_info[sap_id]
        for subject in subjects:
            subjects[subject] += student["marks"][subject]
    for subject in subjects:
        subjects[subject] = int(subjects[subject] / len(student_info))
    return subjects


def number_of_students(student_info: dict) -> int:
    return len(student_info)


def marks_of_each_student_in_a_subject(student_info: dict, subject: str) -> dict:
    subject = subject.lower()
    marks = {}
    for sap_id in student_info:
        student = student_info[sap_id]
        marks[student["name"]] = student["marks"][subject]
    return marks


def marks_of_each_student(student_info: dict) -> dict:
    marks = {}
    for sap_id in student_info:
        student = student_info[sap_id]
        marks[student["name"]] = student["marks"]
    return marks
