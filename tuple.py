print("1. Create a tuple and perform operations")
test_tuple = (1, 2, 3, 4, 5)

print("Traversal:")
for item in test_tuple:
    print(item)

print("\nLength of test_tuple:")
print(len(test_tuple))

print("\nConcatenation of test_tuple and test_tuple2:")
test_tuple2 = (6, 7, 8)
concatenated_test_tuple = test_tuple + test_tuple2
print(concatenated_test_tuple)

print("\nRepetition of test_tuple (repeated twice):")
repeated_test_tuple = test_tuple * 2
print(repeated_test_tuple)

print("\nSlicing test_tuple (from index 1 to 4):")
sliced_test_tuple = test_tuple[1:4]
print(sliced_test_tuple)

print("\nCheck if 3 is in test_tuple and if 6 is in test_tuple:")
print(3 in test_tuple)
print(6 in test_tuple)

print("\nIteration over test_tuple:")
for i in test_tuple:
    print(i)

print("\nCompare test_tuple and test_tuple2:")
print(test_tuple == test_tuple2)

print("\nMaximum and Minimum values in test_tuple:")
print(max(test_tuple))
print(min(test_tuple))

print("\nConvert a list to a tuple:")
test_tuple3 = tuple([10, 20, 30])
print(test_tuple3)

print("\nTuple assignment to variables:")
a, b, c, d, e = test_tuple
print(a, b, c, d, e)

print("\nReturning multiple values using a tuple:")


def return_test_tuple():
    return 1, 2, 3


a, b, c = return_test_tuple()
print(a, b, c)

print("\nNested tuple and print its elements:")
test_tuple4 = (1, (2, 3), (4, 5))
for item in test_tuple4:
    print(item)

print("\nIndex of element 3 in test_tuple:")
print(test_tuple.index(3))

print("\nCount of element 2 in test_tuple:")
print(test_tuple.count(2))

print("\nList comprehension using test_tuple:")
new_test_tuple = tuple(i * 2 for i in test_tuple)
print(new_test_tuple)

print("\nVariable-length argument tuples:")


def variable_length_args(*args):
    print(args)


variable_length_args(1, 2, 3, 4)

print("\nZip function with two tuples:")
test_tuple5 = (1, 2, 3)
test_tuple6 = ("a", "b", "c")
zipped = zip(test_tuple5, test_tuple6)
print(list(zipped))

# 2. Create a tuple with different data types
print("\n2. Create a tuple with different data types")
test_tuple7 = (1, "hello", 3.14, True)
print(test_tuple7)

# 3. Unpack a tuple into several variables
print("\n3. Unpack a tuple into several variables")
test_tuple8 = (10, 20, 30)
a, b, c = test_tuple8
print(a, b, c)

# 4. Add an item to a tuple (create a new one)
print("\n4. Add an item to a tuple (create a new one)")
test_tuple = (1, 2, 3)
new_item = (4,)
test_tuple = test_tuple + new_item
print(test_tuple)

# 5. Convert a tuple to a string
print("\n5. Convert a tuple to a string")
test_tuple9 = ("a", "b", "c")
string = "".join(test_tuple9)
print(string)

# 6. Find repeated items in a tuple
print("\n6. Find repeated items in a tuple")
test_tuple10 = (1, 2, 3, 4, 2, 5, 3)
repeated_items = [item for item in set(test_tuple10) if test_tuple10.count(item) > 1]
print(repeated_items)

# 7. Check whether an element exists within a tuple
print("\n7. Check whether an element exists within a tuple")
test_tuple11 = (1, 2, 3, 4)
print(3 in test_tuple11)
print(5 in test_tuple11)

# 8. Unzip a list of tuples into individual lists
print("\n8. Unzip a list of tuples into individual lists")
list_of_test_tuples = [(1, "a"), (2, "b"), (3, "c")]
unzipped = zip(*list_of_test_tuples)
unzipped_list = [list(item) for item in unzipped]
print(unzipped_list)
