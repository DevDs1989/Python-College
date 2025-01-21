tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)

tuple3 = tuple1 + tuple2


print(tuple3)
print(tuple3[3:9])

del tuple3
try:
    print(tuple3)
except:
    print("Tuple is deleted")


tuple_to_set = set(tuple1)
print(tuple_to_set)
set_to_tuple = tuple(tuple_to_set)
print(set_to_tuple)
print(tuple1 < tuple2)

unsorted = (1, 213, 132, 123, 13, 12321, 3)
sorted_tuple = tuple(sorted(unsorted))
print(sorted_tuple)
print(tuple("HELLO"))

print("Tuple Assigment")
del tuple1
tuple1 = (1, 2, 3)

val1, val2, val3 = tuple1

print(val1, val2, val3)
