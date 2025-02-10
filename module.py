def average(*args):
    print(f"Average: {sum(args) / len(args)}")


def passed(*args):
    count = 0
    for arg in args:
        if arg > 33:
            count += 1
    print(f"Percent of students failed: {count / len(args) * 100}")


def failed(*args):
    count = 0
    for arg in args:
        if arg <= 33:
            count += 1
    print(f"Percent of students failed: {count / len(args) * 100}")
