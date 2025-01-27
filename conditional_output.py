from conditional_function import *

print("divisible by 3 and 5")
n = int(input("Enter a number: "))
check_divisible(n)

print("multiple of 5")
n = int(input("Enter a number: "))
check_multiple(n)

print("maximum of 2 numbers")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
check_max(n1, n2)

print("maximum of 3 numbers")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
n3 = int(input("Enter another number: "))
check_max_3(n1, n2, n3)

print("roots of a quadratic equation")
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))
check_roots(a, b, c)

print("leap year")
year = int(input("Enter a year: "))
if check_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

print("next date")
d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y = int(input("Enter the year: "))
next_date(d, m, y)


name, sapid, sem, course, maths, python, chemistry, english, physics = student_input()
grade_sheet(name, sapid, sem, course, maths, python, chemistry, english, physics)
