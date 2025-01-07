test_list = [10, 12, 122, 13]
print(test_list)

test_list[0] = test_list[0] + test_list[-1]
test_list[-1] = test_list[0] - test_list[-1]
test_list[0] = test_list[0] - test_list[-1]

print(test_list)

sum = 0
for nums in test_list:
    sum += nums
avg = sum / (len(test_list))
print(avg)
