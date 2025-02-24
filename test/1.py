def power_recursion(m, n) -> int:
    if n == 0:
        return 1
    else:
        return m * power_recursion(m, n - 1)


x = int(input("Enter number: "))
y = int(input("Enter power: "))

print(f"{x}^{y} = {power_recursion(x, y)}")
