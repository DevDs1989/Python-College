n = int(input("Enter the number of values: "))
count = {}
valid = set(x for x in range(4))
print("Enter values in range 0-3")
while n:
    n -= 1
    value = int(input())
    if value not in valid:
        print("Invalid value")
        n += 1
    elif value in count:
        count[value] += 1
    else:
        count[value] = 1
for i in sorted(count):
    print(count[i], i)

test_tuple = tuple(x for x in range(1, 21))
print("Tuple: ", test_tuple)
print("Average of all values: ", sum(test_tuple) / len(test_tuple))


n = int(input("Enter the number of students: "))
scores = list()
print("Enter the scores of students")
for i in range(n):
    scores.append(int(input()))
scores_set = set(scores)
print("Runner-up score: ", sorted(scores_set)[-2])


n = int(input("Enter the number of persons: "))
persons = {}
print("Enter the names and cities of persons")
for i in range(n):
    name = input("Enter the name: ")
    city = input("Enter the city: ")
    persons[name] = city
print("Names of all persons: ")
for name in persons.keys():
    print(name)
print("Cities of all persons: ")
for city in set(persons.values()):
    print(city)
print("Details of all persons")
for name, city in persons.items():
    print(name, city)
city_count = {}
for city in persons.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Number of persons in each city")
for city, count in city_count.items():
    print(city, count)


n = int(input("Enter the number of movies: "))
movies = {}
print("Enter the details of movies")
for i in range(n):
    name = input("Enter the name: ")
    year = int(input("Enter the year: "))
    director = input("Enter the director: ")
    production_cost = int(input("Enter the production cost: "))
    collection = int(input("Enter the collection: "))
    movies[name] = {
        "year": year,
        "director": director,
        "production_cost": production_cost,
        "collection": collection,
    }
print("Details of all movies")
for name, details in movies.items():
    print(name, details)
print("Movies released before 2015")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)
print("Movies that made a profit")
for name, details in movies.items():
    if details["collection"] > details["production_cost"]:
        print(name)
director = input("Enter the director name: ")
print("Movies directed by the director")
for name, details in movies.items():
    if details["director"] == director:
        print(name)
