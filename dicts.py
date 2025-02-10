

# print("Dictionary operations")
# dict_test = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

# print("Length of dictionary: ", len(dict_test))

# print("String representation of dictionary: ", str(dict_test))

# dict_test.clear()

# dict_test = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# dict_test_copy = dict_test.copy()
# print("Copy of dictionary: ", dict_test_copy)

# print("Value of key 1: ", dict_test.get(1))

# print("Check if key 1 exists: ", 1 in dict_test)

# print("Items in dictionary: ", dict_test.items())

# print("Keys in dictionary: ", dict_test.keys())

# print("Dictionary from keys: ", dict.fromkeys([1, 2, 3, 4, 5]))

# print("Set default value for key 6: ", dict_test.setdefault(6, "six"))

# dict_test2 = {6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
# dict_test.update(dict_test2)
# print("Updated dictionary: ", dict_test)
# print("Values in dictionary: ", dict_test.values())
# print("Items in dictionary: ", dict_test.items())
# print("x in dict: ", 1 in dict_test)
# print("x not in dict: ", 1 not in dict_test)
# #
# #
# #
# Convert two lists into a dictionary.
# print("Convert two lists into a dictionary")
# keys = ["name", "age", "job"]
# values = ["John", 25, "Developer"]
# dict_test = dict(zip(keys, values))
# print(dict_test)

# # Merge two dictionaries
# print("Merge two dictionaries")
# dict1 = {1: "one", 2: "two", 3: "three"}
# dict2 = {4: "four", 5: "five", 6: "six"}
# dict1.update(dict2)
# print(dict1)

# # Create a dictionary by extracting the keys from a given dictionary
# print("Create a dictionary by extracting the keys from a given dictionary")
# dict_test = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# keys = dict_test.keys()
# dict_test = dict.fromkeys(keys)
# print(dict_test)

# # Delete the list of keys from a dictionary.
# print("Delete the list of keys from a dictionary")
# dict_test = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# keys = [1, 2, 3]
# for key in keys:
#     dict_test.pop(key)
# print(dict_test)
# # # Check if a value exists in a dictionary.
# print("Check if a value exists in a dictionary")
# dict_test = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# if "one" in dict_test.values():
#     print("Value exists")
# else:
#     print("Value does not exist")


# # Minimum value from a dictionary.
# print("Minimum value from a dictionary")
# dict_test = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# print("Minimum value: ", min(dict_test.values()))


# # Sorting dictionary by its key
print("Sorting dictionary by its key")
dict_test = {5: "five", 1: "one", 3: "three", 2: "two", 4: "four"}
sorted_dict = dict(sorted(dict_test.items()))
print(sorted_dict)
