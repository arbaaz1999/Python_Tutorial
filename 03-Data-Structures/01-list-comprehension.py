"""List Comprehension in Python"""

""" 1. for loop vs. list comprehension """
# Using a for loop:

a = [1, 2, 3, 4, 5]

res = []

for val in a:
    res.append(val**2)

print(res)

# Using list comprehension:

a = [1, 2, 3, 4, 5]

res = [val**2 for val in a]

print(res)


""" 2. Conditional statements in list comprehension """

a = [1, 2, 3, 4, 5, 6, 8, 10]

allEven = [val for val in a if val % 2 == 0]

print(allEven)


""" 3. Examples of list comprehension """

# Creating a list from a range :

numList = [val for val in range(10)]

print(numList)


# Using nested loops :

coordinates = [[x, y] for x in range(3) for y in range(3)]

print(type(coordinates[1]))

print(coordinates)


# Flattening a list of lists

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

flatten = [val for row in a for val in row]

print(flatten)


names = ["Arbaz", "Moien", "Amreen"]
scores = [1, 2]

res = zip(names, scores)
print(list(res))
