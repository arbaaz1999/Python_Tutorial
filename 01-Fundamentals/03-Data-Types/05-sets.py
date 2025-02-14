"""Python Sets"""

""" 1. Creating a Set in Python """
set1 = {1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9}
print(type(set1))
print(set1)

# Using set() Function
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks.": 3}
print(set(d))


# Unordered, Unindexed and Mutability
# Creating a set
set1 = {3, 1, 4, 1, 5, 9, 2}

# Unordered: The order of elements is not preserved
print(set1)  # Output may vary: {1, 2, 3, 4, 5, 9}

# Unindexed: Accessing elements by index is not possible
# This will raise a TypeError
try:
    print(set1[0])
except TypeError as e:
    print(e)


""" 2. Adding Elements to a Set in Python """
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)


""" 3. Accessing a Set in Python """
set1 = set(["Geeks", "For", "Geeks."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Geeks" in set1)

""" 4. Removing Elements from the Set in Python """
# a. Using remove() Method or discard() Method
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)

# Using discard() Method
set1.discard(4)
print(set1)

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)

# b. Using pop() Method
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)


# c. Using clear() Method
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)


""" 5. Typecasting Objects into Sets """
# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)


""" frozenset() in Python """

animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals)
print("elephant" in animals)


fruits = frozenset(["apple", "banana", "orange"])
print(fruits)
# fruits.add("cherry")  # will throw an error, because frozenset is immutable.
print(fruits)


# Python frozenset for Tuple
# passing an empty tuple
nu = ()

# converting tuple to frozenset
fnum = frozenset(nu)

# printing empty frozenset object
print("frozenset Object is : ", fnum)


# Python frozenset for List
list1 = ["Geeks", "for", "Geeks"]

# converting list to frozenset
fnum = frozenset(list1)

# printing empty frozenset object
print("frozenset Object is : ", fnum)

# frozenset in Python for Dictionary
# creating a dictionary
Student = {
    "name": "Ankit",
    "age": 21,
    "sex": "Male",
    "college": "MNNIT Allahabad",
    "address": "Allahabad",
}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing dict keys as frozenset
print("The frozen set is:", key)


""" Exceptions while using the frozenset() method in Python """
# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]

# creating a frozenset
f_subject = frozenset(favourite_subject)

# below line will generate error
# f_subject[1] = "Networking"


""" Frozenset operations """
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)

# union
union_set = A.union(B)
print(union_set)

# intersection
intersection_set = A.intersection(B)
print(intersection_set)

difference_set = A.difference(B)
print(difference_set)

# symmetric_difference
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)
