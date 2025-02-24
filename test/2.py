def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs


num = int(input("Enter number of array elements: "))
arr = []

for i in range(num):
    temp = int(input(f"Enter array element {i + 1}:"))
    arr.append(temp)

target = int(input("Enter target:"))

if len(find_pairs(arr, target)) == 0:
    print("No pairs found")
else:
    print(find_pairs(arr, target))
