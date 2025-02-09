# 1. Numeric Data Types in Python
# a. Integer
a = 5
print("type of a is : ", type(a))  # <class 'int'>

# Python int() Function Examples
print("int('9') : ", int("9"))  # int() function  with string

print("int('9.9) : ", int(9.9))  # int() function with float numbers

print("int(9) : ", int(9))  # int() function with interger value

# Convert base using int() in Python
# octal to decimal using int()
print("int() on 0o12 =", int("0o12", 8))

# binary to decimal using int()
print("int() on 0b110 =", int("0b110", 2))

# hexa-decimal to decimal using int()
print("int() on 0x1A =", int("0x1A", 16))


# b. Float
b = 5.5
print(type(b))  # <class 'float'>

# float() in Python
num = float(10)
print("float(10) : ", num)

# Python program to illustrate
# Various examples and working of float()
# for integers
print("float(21.89) : ", float(21.89))

# for floating point numbers
print("float(8) : ", float(8))

# for integer type strings
print('float("23") : ', float("23"))

# for floating type strings
print('float("-16.54") : ', float("-16.54"))

# for string floats with whitespaces
print('float("      -24.45      \\n") : ', float("     -24.45   \n"))

# for inf/infinity
print("float(InF) : ", float("InF"))
print('float("InFiNiTy") : ', float("InFiNiTy"))

# for NaN
print('float("nan") : ', float("nan"))
print('float("NaN") : ', float("NaN"))


# c. Complex Numbers
c = 2 + 4j
print(type(c))  # <class 'complex'>

# Python complex() Function
print("complex(1, 2) : ", complex(1, 2))

z = complex()
print("complex() with no parameters:", z)


# integer type
# passing first parameter only
complex_num1 = complex(5)
print("Int: first parameter only", complex_num1)

# passing both parameters
complex_num2 = complex(7, 2)
print("Int: both parameters", complex_num2)

# float type
# passing first parameter only
complex_num3 = complex(3.6)
print("Float: first parameter only", complex_num3)

# passing both parameters
complex_num4 = complex(3.6, 8.1)
print("Float: both parameters", complex_num4)
