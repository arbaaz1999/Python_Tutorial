"""Polymorphism in PythonJ"""

# Polymorphism is a foundational concept in programming that allows entities like functions, methods or operators to behave differently based on the type of data they are handling.

""" 1. Polymorphism in Built-in Functions """

print("Length of a string : ", len("Hello"))  # String length
print("Length of a List : ", len([1, 2, 3]))  # Length of list

print("Max of numbers : ", max([3, 5, 2]))  # maximum of numbers
print("Max of characters : ", max(["z", "a", "m"]))  # maximum of characters


""" 2. Polymorphism in Functions """


def add(a, b):
    return a + b