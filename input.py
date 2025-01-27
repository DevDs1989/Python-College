from math import pi

x = 9
y = 7

print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")


r = int(input("Enter the radius: "))
area = pi * r**2
print(f"Area of a circle: {area}")


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = (x + y) * (x + y)
print(f"Result: {z}")

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = (a**2 + b**2) ** 0.5
print(f"The length of the hypotenuse is: {c}")


p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))
interest = (p * r * t) / 100
print(f"The simple interest is: {interest}")

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
semi = (a + b + c) / 2
area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5
print(f"The area of the triangle is: {area}")

input_seconds = int(input("Enter the number of seconds: "))
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
seconds = (input_seconds % 3600) % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

x = 5
y = 7
print(f"x: {x}, y: {y}")
x = x + y
y = x - y
x = x - y
print(f"After Swap\nx: {x}, y: {y}")

n = 10
sum = n * (n + 1) / 2
print(f"Sum of first {n} natural numbers: {sum}")

print("Truth table for bitwise AND")
print("A\tB\tA & B")
print("0\t0\t", 0 & 0)
print("0\t1\t", 0 & 1)
print("1\t0\t", 1 & 0)
print("1\t1\t", 1 & 1)
print("Truth table for bitwise OR")
print("A\tB\tA | B")
print("0\t0\t", 0 | 0)
print("0\t1\t", 0 | 1)
print("1\t0\t", 1 | 0)
print("1\t1\t", 1 | 1)
print("Truth table for bitwise XOR")
print("A\tB\tA ^ B")
print("0\t0\t", 0 ^ 0)
print("0\t1\t", 0 ^ 1)
print("1\t0\t", 1 ^ 0)
print("1\t1\t", 1 ^ 1)

x = int(input("Enter a number: "))
left_shift = x << 1
right_shift = x >> 1
print(f"Left shift: {left_shift}")
print(f"Right shift: {right_shift}")

sequence = [10, 20, 56, 78, 89]
x = int(input("Enter a number: "))
if x in sequence:
    print(f"{x} is in the sequence")
else:
    print(f"{x} is not in the sequence")

test_string = "Hello"
char = input("Enter a character: ")
if char in test_string:
    print(f"{char} is in the string")
else:
    print(f"{char} is not in the string")
