import attendance_module as am

student_list = []
student1 = am.student(
    590017127,
    name="Devesh",
    classroom_max=20,
    classroom_attended=15,
    sport_max=12,
    sport_attended=10,
    co_curricular_max=1,
    co_curricular_attended=1,
)
student_list.append(student1)
student2 = am.student(
    590017962,
    name="Priya",
    classroom_max=20,
    classroom_attended=11,
    sport_max=0,
    sport_attended=0,
    co_curricular_max=1,
    co_curricular_attended=1,
)
student_list.append(student2)
student3 = am.student(
    590019208,
    name="Ananya",
    classroom_max=20,
    classroom_attended=8,
    sport_max=12,
    sport_attended=8,
    co_curricular_max=5,
    co_curricular_attended=3,
)
student_list.append(student3)

student4 = am.student(
    sap_id=590017604,
    name="Ayush",
    classroom_max=20,
    classroom_attended=10,
    sport_max=12,
    sport_attended=6,
    co_curricular_max=5,
    co_curricular_attended=0,
)
student_list.append(student4)


def main():
    while True:
        print("\n1. Print student info")
        print("2. Print all students info")
        print("3. Print debarred students")
        print("4. Enter new student")
        print("5. Check debar")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            sap_id = int(input("Enter sap id: "))
            student = am.search_student(student_list, sap_id)
            if student:
                student.print_info()
            else:
                print("Student not found")
        elif choice == 2:
            am.print_all_students(student_list)
        elif choice == 3:
            am.print_debarred_students(student_list)
        elif choice == 4:
            sap_id = int(input("Enter sap id: "))
            name = input("Enter name: ")
            classroom_max = int(input("Enter classroom max: "))
            classroom_attended = int(input("Enter classroom attended: "))
            sport_max = int(input("Enter sport max: "))
            sport_attended = int(input("Enter sport attended: "))
            co_curricular_max = int(input("Enter co-curricular max: "))
            co_curricular_attended = int(input("Enter co-curricular attended: "))
            student = am.student(
                sap_id,
                name,
                classroom_max,
                classroom_attended,
                sport_max,
                sport_attended,
                co_curricular_max,
                co_curricular_attended,
            )
            student_list.append(student)
        elif choice == 5:
            sap_id = int(input("Enter sap id: "))
            student = am.search_student(student_list, sap_id)
            if student:
                if student.check_debar():
                    print("Student is debarred")
                else:
                    print("Student is not debarred")
            else:
                print("Student not found")
        else:
            break


if __name__ == "__main__":
    main()
