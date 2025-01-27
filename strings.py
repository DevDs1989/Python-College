multiline_string = """Using
multiple
lines
"""
print(multiline_string)

a = input("Enter a string: ")
b = input("Enter b string: ")
print("a+b: ", a + b)
print("a*3: ", a * 3)


try:
    a[3] = "m"
except TypeError:
    print("Strings are immutable")


print("Indexing")
print("a[0]: ", a[0])
print("a[-1]: ", a[-1])

print("Slicing")
print("a[0:3]: ", a[0:3])
print("a[::-1]: ", a[::-1])

print("String methods")
print("capitalize(): ", a.capitalize())
print("center(20, '*'): ", a.center(20, "*"))
print("count('l'): ", a.count("l"))
print("endswith('o'): ", a.endswith("o"))
print("find('l'): ", a.find("l"))
print("rfind('l'): ", a.rfind("l"))
print("isalnum(): ", a.isalnum())
print("isdigit(): ", a.isdigit())
print("index('l'): ", a.index("l"))
print("rindex('l'): ", a.rindex("l"))
print("isalpha(): ", a.isalpha())
print("islower(): ", a.islower())
print("isspace(): ", a.isspace())
print("isupper(): ", a.isupper())
print("len(a): ", len(a))
print("ljust(20, '*'): ", a.ljust(20, "*"))
print("rjust(20, '*'): ", a.rjust(20, "*"))
print("upper(): ", a.upper())
print("lower(): ", a.lower())
print("split(): ", a.split())
print("join(): ", " ".join(a))
print("count('l'): ", a.count("l"))
print("replace('l', 'm'): ", a.replace("l", "m"))
print("rstrip(): ", a.rstrip())

print("Unicode")
ch = "R"
print(ord(ch))
print(chr(112))

a = "Name = %s and Age = %d" % ("Anika", 6)
print(a)
print("{0},eggs and {1}".format("span", "SPAN!"))
print("{1},eggs and {0}".format("span", "SPAN!"))
print("{},eggs and {}".format("span", "SPAN!"))


print("palindrome check")


def is_palindrome(s):
    if s == s[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


s = input("Enter a string: ")
is_palindrome(s)

print("String Character number")
s = input("Enter a string: ")
print(f"number of characters is {len(s)}")

print("number of vowels")
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

print("same chars in 2 strings")
a = input("Enter a string a: ")
b = input("Enter a string b: ")
count = 0
for char in a:
    if char in b:
        count += 1
print(f"Number of common characters: {count}")

print("remove ith character from a string")
s = input("Enter a string: ")
i = int(input("Enter the position of the character to remove: "))
updated_s = s[:i] + s[i + 1 :]
print(f"String after removing the character: {updated_s}")

print("reverse words in a string")
s = input("Enter a string: ")
words = s.split()
print(type(words))
words = words[::-1]
print(" ".join(words))

print("Input two strings and display uncommon words among this pair of strings")
a = input("Enter a string a: ")
b = input("Enter a string b: ")
a_words = a.split()
b_words = b.split()
uncommon_words = []
for word in a_words:
    if word not in b_words:
        uncommon_words.append(word)
for word in b_words:
    if word not in a_words:
        uncommon_words.append(word)
print("Uncommon words: ", uncommon_words)
