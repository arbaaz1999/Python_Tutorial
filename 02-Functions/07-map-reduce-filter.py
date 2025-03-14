"""1. Python map() function"""

# Basic Example : Converting a list of string into a list of integer.

from functools import reduce
from itertools import accumulate
import operator
import time


s = ["1", "2", "3", "4", "5"]

nums = list(map(int, s))
print("Basic example of a map function", nums)


""" 1.1. Converting map object to a list """
a = [1, 2, 3, 4, 5]


def fun(val):
    return val * 2


res = list(
    map(fun, a)
)  # map() functions returns a map object, so converting it into list

print("Map object converted into list : ", res)


""" 1.2. map() with lambda """
a = [1, 2, 3, 4]

res = list(map(lambda x: x * 2, a))

print("Map with lambda function : ", res)


""" 1.3. Using map() with multiple iterables """
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

res = list(map(lambda x, y: x + y, a, b))

print("Map with multiple iterators : ", res)


""" 1.4. Examples of map() function """
# Converting to uppercase
fruits = ["apple", "banana", "mango"]
res = list(map(str.upper, fruits))
print("Converted list of lowercase strings into uppercase using map : ", res)


# Extracting first character from strings
def first_letter(s: str) -> str:
    first = str(s[0]).upper()
    return first


res = list(map(first_letter, fruits))
print("Extracted the first letter of each string in the list using map : ", res)


# Removing whitespaces from strings
s = ["  hello  ", "  world ", " python  "]
res = list(map(str.strip, s))
print("Removed whitespaces of each string using map : ", res)


# Calculate fahrenheit from celsius
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print("Converted celsius into fahrenheit : ", fahrenheit)

""" ------------------------------ x x x map x x x ------------------------------ """


""" 2. reduce() in Python """

# Basic Example : Sum up all the numbers in the list.


def sum(x, y):
    return x + y


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_time = time.time()
res = reduce(sum, a)
diff1 = time.time() - start_time
print("Time taken by reduce without lambda : ", diff1)
print("Sum of all numbers in the list using reduce method : ", res)


""" 2.1. Using reduce() with lambda """
start_time = time.time()
res = reduce(lambda x, y: x + y, a)
diff2 = time.time() - start_time
print("Time taken by reduce with lambda : ", diff2)
print("Sum using reduce with lambda : ", res)


""" 2.2. Using reduce() with operator functions """
print(
    "Sum of all numbers using reduce with operator function : ", reduce(operator.add, a)
)

print(
    "Product of all numbers using reduce with operator function : ",
    reduce(operator.mul, a),
)

print(
    "Addition of all string using reduce with operator function : ",
    reduce(operator.mul, a),
)


""" 2.3. Difference Between reduce() and accumulate() """
"""
The accumulate() function from the itertools module also performs cumulative operations, but it returns an iterator containing intermediate results, unlike reduce(), which returns a single final value.
"""

res = list(accumulate(a, operator.add))
print("Sum using accumulate() : ", res)


""" 3. filter() in python """


# Basic Example : Function to check if a number is even
def even(n):
    return n % 2 == 0


a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

# Convert filter object to a list
print("Returning the list of even numbers using filter() function : ", list(b))


""" 3.1. Using filter() with lambda """
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print("List of even numbers using filter() with lambda : ", list(b))


""" 3.2 Combining filter() with Other Functions """
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)  # filter even numbers from list a
c = list(
    map(lambda x: x * 2, b)
)  # multiply all numbers of filtered list b and store the result in c
print(
    "Combining filter() function with Other functions : ", c
)  # finally print the list c.
