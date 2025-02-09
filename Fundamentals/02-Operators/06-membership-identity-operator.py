import operator

# Python Membership and Identity Operators

# 1. Python Membership Operators
"""
a. Python IN Operator
The IN operator is used to check if a character/substring/element exists in a sequence or not. Evaluate to True if it finds the specified element in a sequence otherwise False.
"""

# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
dict1 = {1: "Geeks", 2: "for", 3: "geeks"}

# using membership 'in' operator
# checking an integer in a list
print(2 in list1)

# checking a character in a string
print("O" in str1)


# checking for a key in a dictionary
print(3 in dict1)

"""
b. Python NOT IN Operator
The NOT IN Python operator evaluates to true if it does not find the variable in the specified sequence and false otherwise.
"""

# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
dict1 = {1: "Geeks", 2: "for", 3: "geeks"}

# using membership 'not in' operator
# checking an integer in a list
print(2 not in list1)

# checking a character in a string
print("O" not in str1)

# checking for a key in a dictionary
print(3 not in dict1)


# 2. Python Identity Operators
"""
a. Python IS Operator
The IS operator evaluates to True if the variables on either side of the operator point to the same object in the memory and false otherwise.
"""
# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is num2)  # True
print(a is b)  # False
print(a is c)  # True
print(s1 is s2)  # True
print(s1 is s2)  # True


"""
b. Python IS NOT Operator
The is not operator evaluates True if both variables on the either side of the operator are not the same object in the memory location otherwise it evaluates False.
"""
# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

# using 'is not' identity operator on different datatypes
print(num1 is not num2)
print(a is not b)
print(a is not c)
print(s1 is not s2)
print(s1 is not s1)


# 3. operator.contain() Method :

# using operator.contain()
# checking an integer in a list
print(operator.contains([1, 2, 3, 4, 5], 2))

# checking a character in a string
print(operator.contains("Hello World", "O"))

# checking an integer in aset
print(operator.contains({1, 2, 3, 4, 5}, 6))

# checking for a key in a dictionary
print(operator.contains({1: "Geeks", 2: "for", 3: "geeks"}, 3))

# checking for an integer in a tuple
print(operator.contains((1, 2, 3, 4, 5), 9))


"""
Note : While comparing objects, The equality operator (==) is used to compare the value of two variables, whereas the identities operator (IS) is used to compare the memory location of two variables.
"""
# Example :
# Python program to illustrate the use
# of 'is' and '==' operators
a = [1, 2, 3]
b = [1, 2, 3]

# using 'is' and '==' operators
print(a is b)
print(a == b)
