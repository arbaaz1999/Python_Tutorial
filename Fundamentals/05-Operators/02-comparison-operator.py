# Comparison Operators in Python (>, <, ==, !=, >=, <=)

a = 9
b = 5
c = 9

print(f"a = {a}, b = {b}, c = {c}")

# 1. Equality Operator (== and is) :
print("a == b : ", a == b)
print("a is b : ", a is b)
"""
“is” returns True if two variables point to the same object.
“==” returns True if two variables have same values (or content).
"""

# 2. Inequality Operator (!=) :
print("a != b : ", a != b)  # return True if both values are not equal
print("a != c : ", a != c)  # else False

# 3. Greater than Sign (>) :
print("a > b : ", a > b)  # Returns True if first values is greater than second
print("b > a : ", b > a)  # Else False

# 4. Less than Sign (<) :
print("a < b : ", a < b)  # Return True if first value is less than second
print("b < a : ", b < a)  # Else False

# 5. Greater than or Equal to Sign (>=) :
print("a >= b : ", a >= b)  # If first value is greater than or equal to second value
print("a >= c : ", a >= c)  # It returns True
print("b >= a : ", b >= a)  # Else False

# 6. Less than or Equal to Sign (<=) :
print("a <= b : ", a <= b)  # If first value is less than or equal to second value
print("a <= c : ", a <= c)  # It returns True
print("b <= a : ", b <= a)  # Else False


# 7. Chaining Comparison Operators
print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a * 10 == 50)
