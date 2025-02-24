# 1.      Write a Python program to find the intersection of two lists without using built-in functions.


def intersection(list1, list2):
    return [i for i in list1 if i in list2]


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = intersection(list1, list2)
print(list3)


# 2.      Write a Python program to find the common elements in three lists.
def common_elements(list1, list2, list3):
    return [i for i in list1 if i in list2 and i in list3]


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [4, 5, 9, 10, 11]
list4 = common_elements(list1, list2, list3)
print(list4)


# 3.      Write a Python program to find the most frequent element in a list.
def mode(list):
    return max(set(list), key=list.count)


list1 = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(mode(list1))


# 4.      Write a Python program to flatten a nested list into a single list.
def flatten(list):
    return [i for sublist in list for i in sublist]


list1 = [[1, 2, 3], [4, 5], [6, 7]]
print(list1)
print(flatten(list1))


# 5.      Write a Python function to find the longest common prefix in a list of strings.
def common_prefix(list):
    for i in range(len(list[0])):
        for string in list[1:]:
            if i >= len(string) or string[i] != list[0][i]:
                return list[0][:i]


list1 = ["flower", "flow", "flight"]
print(common_prefix(list1))


# 6.      Write a program to reverse each word in a string but keep the words in the original order.
def reverse_words(string):
    for word in string.split():
        string = string.replace(word, word[::-1])
    return string


string = "Hello How Are You"
print(reverse_words(string))


# 7.      Write a Python function to check if two strings are anagrams of each other.
def anagram(string1, string2):
    return sorted(string1) == sorted(string2)


print(anagram("listen", "silent"))
print(anagram("hello", "world"))


# 8.      Write a Python program to check if a key exists in a dictionary.
def check_key(dictionary, key):
    return key in dictionary


dict1 = {"a": 1, "b": 2, "c": 3}
print(check_key(dict1, "a"))
print(check_key(dict1, "d"))


# 9.      Write a Python program to count the frequency of characters in a string and store it in a dictionary.
def frequency(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


string = "hello"
print(frequency(string))


# 10. Write a Python function to remove all even numbers from a set.
def remove_even(set):
    return {i for i in set if i % 2 != 0}


set1 = set([i for i in range(20)])
res = remove_even(set1)
print(res)


# 11. Write a Python program to convert a dictionary into a list of tuples.


dict1 = {"a": 1, "b": 2, "c": 3}
print([(x, y) for x, y in dict1.items()])


# 12. Write a Python program to add a key-value pair to a dictionary if it does not exist.
def add_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    return dictionary


dict1 = {"a": 1, "b": 2, "c": 3}
print(add_key(dict1, "d", 4))


# 13. Write a Python program to find all common elements in two dictionaries.
def common_elements(dict1, dict2):
    return {x: dict1[x] for x in dict1 if x in dict2}


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2, "d": 4}
print(common_elements(dict1, dict2))


# 14. Write a Python program to find the greatest common divisor (GCD) using recursion.
def gcd(m, n):
    if m == n:
        return m
    if m > n:
        return gcd(m - n, n)
    else:
        return gcd(m, n - m)


print(gcd(12, 14))


# 15. Write a Python program to implement the power set of a set.
def power_set(set):
    result = [[]]
    for i in set:
        result += [j + [i] for j in result]
    return result


set1 = {1, 2, 3}
print(power_set(set1))


# 16. Write a Python function to find the sum of all elements in a list using recursion.
def sum_recursion(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_recursion(list[1:])


list1 = [1, 2, 3, 4, 5]
print(sum_recursion(list1))


# 17. Write a Python program to merge two dictionaries into one.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
dict1.update(dict2)


# 18. Create a function that accepts a dictionary and returns a list of keys that have integer values.
def int_keys(dictionary):
    return [x for x in dictionary if type(dictionary[x]) == int]


dict1 = {"a": 1, "b": "hello", "c": 3}
print(int_keys(dict1))


# 19. Write a Python program to find the sum of all values in a dictionary.
def sum_values(dictionary):
    return sum(dictionary.values())


dict1 = {"a": 1, "b": 2, "c": 3}
print(sum_values(dict1))


# 20. Write a Python program to find the common keys between two dictionaries.
def common_keys(dict1, dict2):
    return {x for x in dict1 if x in dict2}


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2, "d": 4}
print(common_keys(dict1, dict2))


# 21. Given a dictionary of items and their prices, write a function to calculate the total cost of all items.
dict1 = {"apple": 1, "banana": 2, "orange": 3}
print(sum(dict1.values()))


# 22. Write a Python program to calculate the power of a number using recursion.
def power_recursion(m, n):
    if n == 0:
        return 1
    else:
        return m * power_recursion(m, n - 1)


print(power_recursion(2, 3))


# 23. Write a Python program to check if a string is a valid palindrome considering spaces and punctuation.
def is_palindrome(string):
    string = "".join(e for e in string if e.isalnum()).lower()
    return string == string[::-1]


string = "race car"
print(is_palindrome(string))

# 24. Write a Python program to find all unique pairs in an array that add up to a specific sum.
