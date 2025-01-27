def check_divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by 3 and 5")
    else:
        print(f"{num} is not divisible by 3 and 5")


def check_multiple(num):
    if num % 5 == 0:
        print(f"{num} is a multiple of 5")
    else:
        print(f"{num} is not a multiple of 5")


def check_max(num1, num2):
    if num1 == num2:
        print("Numbers are equal")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")


def check_max_3(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")


def check_roots(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        root1 = (-b + d**0.5) / (2 * a)
        root2 = (-b - d**0.5) / (2 * a)
        print(f"Roots are real and distinct: {root1}, {root2}")
    elif d == 0:
        root = -b / (2 * a)
        print(f"Roots are real and equal: {root}")
    else:
        real = -b / (2 * a)
        imaginary = (-d) ** 0.5 / (2 * a)
        print(f"Roots are imaginary: {real} + {imaginary}i, {real} - {imaginary}i")


def check_leap_year(year):
    if year % 400 == 0:
        return 1
    elif year % 100 == 0:
        return 0
    elif year % 4 == 0:
        return 1
    else:
        return 0


def next_date(day, month, year):
    if month in [1, 3, 5, 7, 8, 10]:
        if day < 31:
            day += 1
        else:
            day = 1
            month += 1
    elif month in [4, 6, 9, 11]:
        if day < 30:
            day += 1
        else:
            day = 1
            month += 1
    elif month == 12:
        if day < 31:
            day += 1
        else:
            day = 1
            month = 1
            year += 1
    elif month == 2:
        if check_leap_year(year):
            if day < 29:
                day += 1
            else:
                day = 1
                month += 1
        else:
            if day < 28:
                day += 1
            else:
                day = 1
                month += 1
    if month > 12:
        month = 1
        year += 1
    print(f"Next date is: {day}/{month}/{year}")


def student_input():
    name = input("Enter the name of the student: ")
    sapid = input("Enter the SAP ID: ")
    sem = input("Enter the semester: ")
    course = input("Enter the course: ")
    print("Enter the marks of the following subjects")
    maths = int(input("Maths: "))
    python = int(input("Python: "))
    chemistry = int(input("Chemistry: "))
    english = int(input("English: "))
    physics = int(input("Physics: "))
    return name, sapid, sem, course, maths, python, chemistry, english, physics


def grade_sheet(name, sapid, sem, course, maths, python, chemistry, english, physics):
    print(f"Name: {name}")
    print(f"SAP ID: {sapid}")
    print(f"Semester: {sem}")
    print(f"Course: {course}")
    print("Subject name: Marks")
    print(f"Maths: {maths}")
    print(f"Python: {python}")
    print(f"Chemistry: {chemistry}")
    print(f"English: {english}")
    print(f"Physics: {physics}")
    percentage = (maths + python + chemistry + english + physics) / 5
    cgpa = percentage / 10
    print(f"Percentage: {percentage}%")
    print(f"CGPA: {cgpa}")
    if cgpa >= 9.1:
        grade = "O"
    elif cgpa >= 8.1:
        grade = "A+"
    elif cgpa >= 7.1:
        grade = "A"
    elif cgpa >= 6.1:
        grade = "B+"
    elif cgpa >= 5.1:
        grade = "B"
    elif cgpa >= 3.5:
        grade = "C+"
    else:
        grade = "F"
    print(f"Grade: {grade}")
