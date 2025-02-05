# def add_two(n, m):
#     return (n + m) / 2


# x = int(input("Enter 1st number: "))
# y = int(input("Enter 2nd number: "))
# z = add_two(m=x, n=y)
#


def using_default(name="No Name"):
    print("Hello, " + name)


# using_default()


def favorite_subjects(name, *fave_subjects):
    print(name + "'s favorite subjects are:")
    for subject in fave_subjects:
        print(subject)


# favorite_subjects("Devesh", "Math", "Science", "English")

add_two = lambda name="NONE": "Hello, " + name

print(add_two(name="Devesh"))
