test_list = [1, 12, 123, 1, 2, 213, 1, 22, 2, 33, 3]

max = test_list[0]
i = 0
for num in test_list:
    if num > max:
        max = num

for nums in test_list:
    if nums == max:
        test_list.pop(i)
        break
    i = i + 1

second_max = test_list[0]
for num in test_list:
    if num > second_max:
        second_max = num

test_list.append(max)
print(second_max)
print(test_list)
