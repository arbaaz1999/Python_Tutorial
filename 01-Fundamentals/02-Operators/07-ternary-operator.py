# Python Ternary Operator

# Basic Example of Ternary Operator
# Example : To check whether the number is Even or Odd
n = 5
isEven = "Even" if n % 2 == 0 else "Odd"
print(f"{n} is {isEven}")


# Ternary Operator in Nested If else
# Example : To check whether the number is negative, positive or zero
n = 0
result = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(f"{n} is {result}")


# Ternary Operator using Tuple
# Example : To check whether the number is Even or Odd
n = 33
res = ("Odd", "Even")[n % 2 == 0]
print(f"{n} is {res} using Tuple")


# Ternary Operator using Dictionary
# Example : Find the maximum of two numbers
a = 10.0000000002
b = 10.0000000001
res = {True: a, False: b}[a > b]
print(f"{res} is greater. Using Dictionary.")


# Ternary Operator using Python Lambda
# Example : Find the maximum of two numbers
a = 10.0000000002
b = 10.0000000001
res = (lambda x, y: x if x > y else y)(a, b)
print(f"{res} is greater, Using Lambda.")


# Ternary Operator with Print Function
a = 10
b = 20
print("a is greater" if a > b else "b is greater")
