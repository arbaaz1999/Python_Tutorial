"""Python Lists"""

""" 1. Creating a List : """
# a. Using Square Brackets
# List of integers

a = [1, 2, 3, 4, 5]

# List of strings
b = ["apple", "banana", "cherry"]

# Mixed data types
c = [1, "hello", 3.14, True]

print("List of Integers : ", a)
print("List of Strings : ", b)
print("List of Mixed Data Types : ", c)

# Using list() Constructor
a = list((1, 2, 3, 4.5, "this is string", True))

print("List using list() constructor : ", a)


""" 2. Creating List with Repeated Elements """
a = [2] * 8
b = [0] * 6
print("List of Repeating Elements using * operator : ", a)
print("List of Repeating Elements using * operator : ", b)


""" 3. Accessing List Elements """
a = [1, 2, 3, 4, 5, 6]

print("Access first element : ", a[0])
print("Access last element : ", a[-1])


""" 4. Adding Elements into List """
a = []
a.append(5)
print("a.append(5) -> Adds Element to the last position : ", a)

a.insert(0, 10)
print("a.insert(0, 10) -> Adds element 10 at 0th indes : ", a)

a.extend([20, 15, 30, 25])
print("a.extend([20, 15, 30, 25]) -> Adds multiple elements at the end : ", a)


""" 5. Updating Elements into List """
a = [10, 5, 7, 13, 9]

a[2] = 11
print("Changed the third element in the list : ", a)


""" 6. Removing Elements from List """
a = [11, 9, 7, 5, 3, 1]

a.remove(7)
print("a.remove(7) -> Removes the element 7 from the list : ", a)

poped_value = a.pop(1)
print("Popped Value : ", poped_value)
print("a.pop(1) -> Removes the element from index 1 : ", a)

del a[0]
print("After deleting element at 0th index : ", a)


""" 7. Iterating Over Lists """
a = [
    "apple",
    "banana",
    "mango",
    1,
    2.5,
    5,
    True,
    False,
    {
        "isFood": True,
    },
]

for i in a:
    print(f"{i}")


""" 8. Nested Lists in Python """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print("Access the element of 2d array -> matrix[1][1] : ", matrix[1][1])
