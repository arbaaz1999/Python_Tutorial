import sys

sys.stdout.write("This is some output data ! \n")

# In this section, we will discussing input and output

# Printing the String on the screen
print("Some String")

# Printing Single Variable
name = "Bob"
print(name)

# Printing Multiple Variables
name_two = "Alice"
age = 23
is_male = True

print(name_two, age, is_male)  # Separated by commas (,)


# Output Formatting
# Using Format() method

price = 150.75
print("Price of the Item is $ {:.2f}".format(price))

# Using sep="" and end="" parameter

# 'end' parameter with '@'
print("Python", end="@")
print("GeeksForGeeks")

# separating with commas
print("Apple", "Mango", "Banana", sep=", ")

# for formatting a date
print("09", "12", "2016", sep="-")

# another example
print("pratik", "geeksforgeeks", sep="@")

print(0.1 + 0.2 == 0.3)

# Using f-string
my_name = "Arbaaz"
course = "Python"
source = "GeeksForGeeks"

print(f"Hi! My name is {my_name} and I am learning {course} from {source}")


# Using % Operator
"""
%d –integer
%f – float
%s – string
%x –hexadecimal
%o – octal
"""

this_is_float = 25.43257
this_is_integer = 67
this_is_string = "Hello Geeks!"

print ("Float is %f" %this_is_float)
print("Integer is %d" %this_is_integer)
print("String is %s" %this_is_string)

# Taking Multiple Inputs in Python :
""" x, y , z = input("Enter Three Numbers").split()

print("First value is : ", x)
print("Second value is : ", y)
print("Third value is : ", z) """


# Type Casting in Python using int(), str(), float() methods

""" your_name = input("Enter Your Name : ")
str(your_name) #Type Casted the input to string 

your_age = int(input("What's your age ? "))

your_height = float(input("Enter your Height : "))

print(f"Hello {your_name}! Your age is {your_age} and your height is {your_height} cm") """


# Find Data Type of Input in Python

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeksss":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))