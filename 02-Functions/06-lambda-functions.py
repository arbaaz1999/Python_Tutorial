"""Python Lambda or Anonymous Functions"""

from functools import reduce

# Basic Example :


s1 = "geeksforgeeks"
s2 = lambda str: str.upper()  # noqa: E731
print("String converted to upper case using lambda function : ", s2(s1))


""" 1. lambda with Condition Checking """
num = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"  # noqa: E731
print("Num function : ", num(-3))
print("Num function : ", num(0))
print("Num function : ", num(5))


""" 2. Lambda with if-else """
check = lambda x: "Even" if x % 2 == 0 else "Odd"  # noqa: E731
print("Even or Odd -> 8 : ", check(8))
print("Even or Odd -> 11 : ", check(11))


""" 3. Lambda with Multiple Statements """
calc = lambda x, y: (x + y, x * y)  # noqa: E731
print("Calc : ", calc(2, 8))


""" 4. Using lambda with filter() """
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listOfEvenNumbers = filter(lambda x: x % 2 == 0, numbers)
print(type(listOfEvenNumbers))
print("Even Numbers are : ", list(listOfEvenNumbers))


""" 5. Using lambda with map() """
numbers = [1, 2, 3, 4, 5]
doubleNumbers = map(lambda x: x * 2, numbers)
print("Double the numbers : ", list(doubleNumbers))


""" 6. Using lambda with reduce() """
numbers = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers : ", b)
