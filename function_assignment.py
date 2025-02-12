# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)
# def max_min(args: list):
#     max_num = args[0]
#     min_num = args[0]
#     for i in args:
#         if i > max_num:
#             max_num = i
#         if i < min_num:
#             min_num = i
#     return max_num, min_num
#
#
# maximum, minimum = max_min([120, 122, 3, 1212, 31, 31313, 12])
# print(f"Max: {maximum} Min: {minimum}")
#
#
# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
# def sum_of_cubes(n):
#     if n < 0:
#         print("Enter a positive number")
#     sum = 0
#     for i in range(1, n):
#         sum += i**3
#     return sum
#
#
# n = int(input("Enter a number: "))
# print(f"sum of cubes {sum_of_cubes(n)}")


# Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
# def print_recursion(n):
#     if n == 0:
#         return
#     print_recursion(n - 1)
#     print(n)
#
#
# n = int(input("Enter number: "))
# print_recursion(n)


# Write a recursive function to print Fibonacci series upto n terms.
# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# n = int(input("Enter number: "))
# for i in range(n):
#     print(fib(i), end="->")
# Write a lambda function to find volume of cone.
# vol_of_cone = lambda r, h: (1 / 3) * 3.14 * r**2 * h
# r, h = map(int, input("Enter radius and height: ").split())
# print(f"Volume of cone: {vol_of_cone(r, h)}")
#
# Write a lambda function which gives tuple of max and min from a list.
# Sample input: [10, 6, 8, 90, 12, 56]
# Sample output: (90,6)
max_min = lambda tist: (max(tist), min(tist))
test_list = [12, 13, 123, 12, 98]
variable = max_min(test_list)
print(f"tuple {variable}")

# Write functions to explain mentioned concepts:
# Keyword argument
# Default argument
# Variable length argument
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Give an example for creating a function inside a function.
# Write a Python function to check whether a string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# Write a Python function to check whether a number is "Perfect" or not. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself.
