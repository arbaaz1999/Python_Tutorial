# Python Bitwise Operators (&, |, ~, ^, >>, <<)

x = 7  # Binary Representation = 111
y = 4  # Binary Representation = 100

# Bitwise AND Operator (&) :

print(
    "X & Y = ", x & y
)  # performs AND Operation on the bits of both numbers e.g. 1 & 1 = 1, 1 & 0 = 0, 1 & 0 = 0 i.e. 100 = 4

# Bitwise OR Operator (|) :

print(
    "X | Y = ", x | y
)  # performs OR Operation on the bits of both numbers e.g. 1 | 1 = 1, 1 | 0 = 1, 1 | 0 = 1 i.e. 111 = 7

# Bitwise XOR (exclusive OR) Operator (^) :

print(
    "X ^ Y = ", x ^ y
)  # If the bits are different, it returns 1; otherwise, it returns 0 e.g. 1 ^ 1 = 0, 1 ^ 0 = 1, 1 & 0 = 1 i.e. 011 = 3

# Bitwise NOT Operator (~) :

print(
    "~x = ", ~x
)  # it toggles all bits in the value, transforming 0 bits to 1 and 1 bits to 0


"""
Bitwise Right Shift
Shifts the bits of the number to the right and fills 0 on voids left (fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.
"""
a = 99
b = 50

print("x >> 4 = ", a >> 4, "b >> 4 = ", b >> 4)


"""
Bitwise Left Shift
Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
"""

a = 99
b = 50

print("x << 4 = ", a << 4, "b << 4 = ", b << 4)
