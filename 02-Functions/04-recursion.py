"""Recursion in Python"""

""" 1. Basic Example of Recursion: """


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Recursive function example of factorial(5) : ", factorial(5))


""" 2. Base Case and Recursive Case """


def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
print("Base and Recursive Case Example : ", fibonacci(10))


""" 3. Types of Recursion in Python """


# a. Tail Recursion :
"""
This occurs when the recursive call is the last operation executed in the function, with no additional work or calculation following the recursive call.
"""


def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n - 1, acc * n)


# b. Non-Tail Recursion :
"""
This occurs when there are operations or calculations that follow the recursive call.
"""


def non_tail_fact(n):
    if n == 1:
        return 1
    else:
        return n * non_tail_fact(n - 1)


print(tail_fact(5))
print(non_tail_fact(5))