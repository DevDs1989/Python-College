# # factorial of a number
# print("Factorial of a number")
# x = int(input("Enter a number: "))

# for i in range(1, x):
#     x = x * i
# print(x)

# # armstrong number
# print("Armstrong number")
# x = int(input("Enter a number: "))
# temp = x
# result = 0
# n = len(str(x))
# while temp > 0:
#     digit = temp % 10
#     result += digit**n
#     temp = temp // 10
# if result == x:
#     print("Armstrong number")
# else:
#     print("Not an armstrong number")
# # fibonacci series
#
# print("Fibonacci series")
#
#
# def fibonacci(n):
#     a = 0
#     b = 1
#     print(a, end="\t")
#     print(b, end="\t")
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c, end="\t")


# n = int(input("Enter a number: "))
# fibonacci(n)
# # prime number
# print("\nPrime number")
# x = int(input("Enter a number: "))
# if x > 1:
#     for i in range(2, x):
#         if x % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")

# sum of all digits
# print("Sum of all digits")
# x = int(input("Enter a number: "))
# sum = 0
# while x > 0:
#     digit = x % 10
#     sum += digit
#     x = x // 10
# print(sum)


# # palindrome number
# print("Palindrome number")


# def palindrome(n):
#     temp = n
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     if temp == rev:
#         print("Palindrome number")
#     else:
#         print("Not a palindrome number")

# n = int(input("Enter a number: "))
# palindrome(n)

# count and print all the numbers divisible by 5 or 7 between 1 and 100
# print("Numbers divisible by 5 or 7")


# def divisible():
#     for i in range(1, 101):
#         if i % 5 == 0 or i % 7 == 0:
#             print(i)


# divisible()
#
# covert all lowercase to upper case in a string using loop
# print("Convert lowercase to uppercase")
# string = input("Enter a string: ")
# new_string = ""
# for i in string:
#     if i.islower():
#         new_string += i.upper()
#     else:
#         new_string += i
# print(new_string)
# #
# print all prime numbers between 1 and 100
# print("Prime numbers between 1 and 100")
# for i in range(1, 101):
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

# # print the times table for a given number
#
# print("Times table")
#

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


n = int(input("Enter a number: "))
table(n)
