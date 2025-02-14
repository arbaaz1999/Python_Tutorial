"""Python Tuples"""

""" 1. Creating a Tuple """

t = ()  # empty tuple

t = ("geeks", "for")
print("Tuple created using strings : ", t)

t = [1, 2, 3, 4, 5]
print("Tuple created using list of integers : ", tuple(t))


tup = tuple("Geeks")
print("Using Built-in Function", tup)


""" 2. Creating a Tuple with Mixed Datatypes. """
# Creating a Tuple with Mixed Datatype
tup = (5, "Welcome", 7, "Geeks")
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ("python", "geek")
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ("Geeks",) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = "Geeks"
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)


""" 3. Python Tuple Operations """
# a. Accessing of Tuples
# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# b. Concatenation of Tuples
tup1 = (1, 2, 3, 4, 5)
tup2 = ("Geeks", "for", "Geeks")

tup3 = tup1 + tup2
print("tup1 + tup2 = ", tup3)

# c. Slicing of Tuple
# Slicing of a Tuple with Numbers
tup = tuple("GEEKSFORGEEKS")

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])

# d. Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup

# print(tup) # uncommenting this will throw an error


""" Python Boolean Data Type """

print(type(True))
print(type(False))
