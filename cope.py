import copy

test_list = [1, [2, 3], 4, 5]
print(f"Original List: {test_list}")
copy_list = copy.copy(test_list)
print(f"Shallow Copy List: {copy_list}")
deepcopy_list = copy.deepcopy(test_list)
print(f"Deep Copy List: {deepcopy_list}")

test_list[1][0] = 100
print("Changing the value of test_list")
print(f"Original List: {test_list}")
print(f"Shallow Copy List: {copy_list}")
print(f"Deep Copy List {deepcopy_list}")
