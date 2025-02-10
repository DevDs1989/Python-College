import studentModule as sm

students = {}
sm.add_student(students, 590017127, "Devesh", [80, 10, 50])
sm.add_student(students, 590018144, "Dhruv", [80, 70, 60])
sm.add_student(students, 590017604, "Ayush", [30, 30, 12])
sm.add_student(students, 590017962, "Priya", [20, 49, 20])
sm.add_student(students, 590019208, "Ananya", [21, 22, 23])

while True:
    print("\n1. Total Average")
    print("2. Student Average")
    print("3. Percent Passed")
    print("4. Percent Failed")
    print("5. Student Pass")
    print("6. Enter a Student")
    print("7. Show Student information")
    print("8. Average of each subject")
    print("9. Number of students")
    print("10. Marks of each student in a subject")
    print("11. Marks of each student")
    print("12. Exit")
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Total Average: {sm.total_average(students)}")
    elif choice == 2:
        sap_id: int = int(input("Enter SAP ID: "))
        print(f"Student Average: {sm.student_average(students, sap_id)}")
    elif choice == 3:
        print(f"Percent Passed: {sm.percent_passed(students)}")
    elif choice == 4:
        print(f"Percent Failed: {sm.percent_failed(students)}")
    elif choice == 5:
        sap_id: int = int(input("Enter SAP ID: "))
        print(f"Student Pass: {sm.student_pass(students, sap_id)}")
    elif choice == 6:
        sap_id: int = int(input("Enter SAP ID: "))
        name: str = input("Enter Name: ")
        subjects = []
        for subject in ["Maths", "Python", "DSA"]:
            mark = int(input(f"Enter marks for {subject}: "))
            subjects.append(mark)
        sm.add_student(students, sap_id, name, subjects)
    elif choice == 7:
        sm.print_student_info(students)
    elif choice == 8:
        subject_marks = sm.average_per_subject(students)
        for subject, avg in subject_marks.items():
            print(f"{subject}: {avg}")
    elif choice == 9:
        print(f"Number of students: {sm.number_of_students(students)}")
    elif choice == 10:
        subject = input("Enter subject from Maths, Python, DSA: ")
        marks = sm.marks_of_each_student_in_a_subject(students, subject)
        for sap_id, mark in marks.items():
            print(f"{sap_id}: {mark}")
    elif choice == 11:
        marks = sm.marks_of_each_student(students)
        for sap_id, mark in marks.items():
            print(f"{sap_id}".center(20, "-"))
            for subject, marks in mark.items():
                print(f"{subject.capitalize()}: {marks}")
    elif choice == 12:
        break

    else:
        print("Invalid Choice")
