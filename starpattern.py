rows = 5
for i in range(rows):
    print(" " * (rows - i), "*" * (2 * i - 1))
for j in range(rows - 2, -1, -1):
    print(" " * (rows - j), "*" * (2 * j - 1))
