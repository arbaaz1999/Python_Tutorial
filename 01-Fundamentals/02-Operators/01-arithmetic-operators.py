# Python Operators

# 1. Python Arithmetic Operators

val1 = 15
val2 = 9
print(f"val1 = {val1}, val2 = {val2}")

# i. Addition Operator (+) :
result = val1 + val2  # returns the sum of two values
print("Addition ", result)

# ii. Substraction Operator (-) :
result = val1 - val2  # return the difference of two values
print("Substration ", result)

# iii. Multiplication Operator (*) :
result = val1 * val2  # returns the product of two values
print("Multiplication ", result)

# iv. Division Operator (/) :
# a. Float Division :
result = (
    val1 / val2
)  # it divides the first value by second value and returns the reminder -> 5 // 2 = 2.5
print("Float Division ", result)

# b. Floor Division (//) :
result = (
    val1 // val2
)  # The reminder returned by this operator gets floored -> 5 // 2 = 2
print("Floor Division ", result)

# v. Modulus Operator (%)
result = val1 % val2  # it returns the quotient remained after dividing both values
print("Modulus ", result)

# vi. Exponentiation Operator (**) :
result = val1**val2
print("Exponention ", result)
