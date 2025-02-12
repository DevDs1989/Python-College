import csv

# 3. Write a Python program to read the current line from a given CSV file.
# with open("customers-100.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# 4. Write a Python program to read and display the content of a given CSV file.
# 5. Write a program to count the number of lines in a given CSV file.
with open("customers-100.csv", "r") as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        count += 1
    print(f"Number of lines: {count}")

# 6. Write a Python program to create a shallow copy of a given list.
# 7. Write a Python program to create a deep copy of a given list.
# 8. Determine the purpose of the following functions by importing the associated
# random.choice()
# random.random()
# random.randint()
# random.randrange()
# random.uniform()
# random.sample()
# types.LambdaType()
# types.MethodType()
# decimal.Decimal
# Math.sqrt()
# Time.ctime()
# Time.sleep()
#  math.pi
# math.pow()
#  math.trunc()
# math.floor()
#  time.gmtime()
#  sys.version
# sys.modules
#
#
#
#
#
