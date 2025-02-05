print("Capital Letters in a string")
string = input("Enter a string: ")
count = 0
for i in string:
    if i.isupper():
        count += 1
print("Number of capital letters in the string are: ", count)

print("Vowels in a string")
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for i in string:
    if i in vowels:
        count += 1
print("Number of vowels in the string are: ", count)

print("Words in new line")
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

print("Number of times a substring occurs in a string")
string = input("Enter a string: ")
substring = input("Enter a substring: ")
count = 0
for i in range(len(string)):
    if string[i : i + len(substring)] == substring:
        count += 1
print("Number of times the substring occurs in the string are: ", count)

print("Number of occurrences of each alphabet in a string")
string_test = input("Enter a string: ")
string_test = string_test.lower()
count = {}
for i in string_test:
    if i.isalpha():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
for i in sorted(count):
    print(count[i], i)

print("Number of unique words in a sentence")
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words in the sentence are: ", len(unique_words))

print("Create 2 sets s1 and s2 of n fruits each by taking input from user and find")
s1 = set()
s2 = set()
n = int(input("Enter the number of fruits: "))
print("Enter the fruits in set s1")
for i in range(n):
    s1.add(input())
print("Enter the fruits in set s2")
for i in range(n):
    s2.add(input())
print("Fruits which are in both sets s1 and s2 are: ", s1.intersection(s2))
print("Fruits only in s1 but not in s2 are: ", s1.difference(s2))
print("Count of all fruits from s1 and s2 are: ", len(s1) + len(s2))
