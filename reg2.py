import re

# Write a Python program to find all email addresses in a given text using regular expressions.
email1 = "this string has emails devesh.17127@stu.upes.ac.in"
email2 = "this string has emials deveshchandra187@gmail.com"
reg = r"[a-zA-Z0-9._]+@[a-zA-Z.-]+\.[a-z]+"
print(re.findall(reg, email1))
print(re.findall(reg, email2))

# Write a Python program to match dates in the format dd/mm/yyyy using regular expressions.
date1 = "today is 31/12/2020"
date2 = "today is 32/13/2021"
reg = r"\b[0-3][0-9]/[0-1][0-9]/[0-9]{4}\b"
print(re.findall(reg, date1))
print(re.findall(reg, date2))

# Write a Python program to validate a phone number (format: xxx-xxx-xxxx) using regular expressions.
phone1 = "phone number is 123-456-7890"
reg = r"\b[0-9]{3}-[0-9]{3}-[0-9]{4}\b"
print(re.findall(reg, phone1))
# Write a Python program to remove all non-alphanumeric characters from a string using regular expressions.
string = "this string has non-alphanumeric characters 123@abc"
reg = r"[^a-zA-Z0-9]"
print(re.sub(reg, "", string))

# Write a Python program to check if a string contains only digits using regular expressions.
string = "123"
string2 = "123abc"
reg = r"^[0-9]+$"
print(re.match(reg, string))
print(re.match(reg, string2))
# Write a Python program to extract all words that start with a vowel from a string using regular expressions.
string = "apple banana orange"
reg = r"\b[aeiouAEIOU][a-zA-Z]*\b"
print(re.findall(reg, string))

# Write a Python program to replace all occurrences of a word with another word using regular expressions.
string = "this word string has word"
reg = r"\bword\b"
print(re.sub(reg, "WORD", string))
# Write a Python program to check if a string is a valid email address using regular expressions.
email1 = "devesh.17127@stu.upes.ac.in"
email2 = "deveshchandra187@gmailcom"
reg = r"\b[a-za-z0-9._]+@[a-za-z.-]+\.[a-z]+\b"
print(re.match(reg, email1))
print(re.match(reg, email2))


# Write a Python program to split a string by commas using regular expressions.
string = "this string, has, commas"
reg = r","
print(re.split(reg, string))
# Write a Python program to extract all numbers from a string using regular expressions.
string = "this string has 123 numbers 456"
reg = r"[0-9]+"
print(re.findall(reg, string))
