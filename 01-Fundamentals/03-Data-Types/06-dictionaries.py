"""Dictionary Data Type"""

# 1. Create a Dictionary in Python
# Initialize empty dictionary
d = {}


d = {1: "Geeks", 2: "For", 3: "Geeks"}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: "Geeks", 2: "For", 3: "Geeks"})
print(d1)


# Accessing Key-value in Dictionary
d = {1: "Geeks", "name": "For", 3: "Geeks"}

# Accessing an element using key
print(d["name"])

# Accessing a element using get
print(d.get(3))
