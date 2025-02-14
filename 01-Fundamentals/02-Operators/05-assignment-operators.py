# Assignment Operators in Python (=, +=, -=, *=, /=, //=, %=, &=, |=, ^=, >>=, <<=, :=, **=) :

a = 10
b = 3

c = a + b  # Assinging the value using Assignment Operator to the variable c
print("a + b = ", c)


"""
1. Addition Assignment Operator
The Addition Assignment Operator is used to add the right-hand side operand with the left-hand side operand and then assigning the result to the left operand.
"""

a += b  # a = a + b
print("a += b is ", a)

"""
2. Subtraction Assignment Operator
The Subtraction Assignment Operator is used to subtract the right-hand side operand from the left-hand side operand and then assigning the result to the left-hand side operand.
"""

a -= b  # a = a - b
print("a -= b is ", a)

"""
3. Multiplication Assignment Operator
The Multiplication Assignment Operator is used to multiply the right-hand side operand with the left-hand side operand and then assigning the result to the left-hand side operand.
"""

a *= b  # a = a * b
print("a *= b is ", a)


"""
4. Division Assignment Operator
The Division Assignment Operator is used to divide the left-hand side operand with the right-hand side operand and then assigning the result to the left operand.
"""

a /= b  # a = a / b
print("a /= b is ", a)


"""
5. Modulus Assignment Operator
The Modulus Assignment Operator is used to take the modulus, that is, it first divides the operands and then takes the remainder and assigns it to the left operand.
"""

a %= b  # a = a % b
print("a %= b is ", a)


# 6. Floor Division Assignment Operator
a = 11
b = 2

a //= b  # a = a // b
print("a //= b is ", a)

# 7. Exponentiation Assignment Operator

a = 2
b = 3

a **= b  # a = a ** b
print("a **= b is ", a)


# 8. Bitwise AND Assignment Operator

a = 3
b = 5

# a = a & b
a &= b

# Output
print("a &= b is ", a)


# 9. Bitwise OR Assignment Operator

a = 3
b = 5

# a = a | b
a |= b

# Output
print("a |= b is ", a)


# 10. Bitwise XOR Assignment Operator

a = 3
b = 5

# a = a ^ b
a ^= b

# Output
print("a ^= b", a)


# 11. Bitwise Right Shift Assignment Operator

a = 3
b = 5

# a = a >> b
a >>= b

# Output
print("a >>= b is ", a)


# 12. Bitwise Left Shift Assignment Operator

a = 3
b = 5

# a = a << b
a <<= b

# Output
print("a >>= b is ", a)


# 13. Walrus Operator (:=) :
# Example 1 :
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(n)
    numbers.pop()


# Example 2 :
sample_data = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True},
]

print("With Python 3.8 Walrus Operator:")
for entry in sample_data:
    if name := entry.get("name"):
        print(f'Found name: "{name}"')


# Example 3 :
foods1 = list()
while (food := input("What food do you like:=  ")) != "quit":
    foods1.append(food)

for i in range(len(foods1)):
    print(foods1[i])
