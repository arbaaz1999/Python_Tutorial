# Python Variables

v = 10  # Variable 'v' holds the integer value '10'

name = "Rahul"  # Variable 'name' stores the value 'Rahul'

# Basic Assignment using =operator

y = 5
z = 3.14
w = "Hi!"

# Dynamic Typing

p = 76

p = "Now a String"


# Multiple Assignment

# Assigning the same value

d = b = c = 100

print(d, b, c)


# Assigning Different Values

u, y, z = 1, 1.25, "Python"

print(u, y, z)

# Type Casting a Variable

# Casting Variables

s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)
print(f)
print(s2)

# Scope of a variable

# Local Variables


def fun():
    a = "I am a local variable"
    print(a)


fun()
# print(a) # This would raise an error since 'local_var' is not accessible outside the function


# Global Variables

aa = "I am global"


def f():
    global aa
    aa = "Modified globally"
    print(aa)


f()
print(aa)


# Object Reference in Python

x = 5  # Assigning a value 5 to variable x. Here x is referencing to the object with value 5 during execution

y = x  # Now if we assign the variable x to another variable y. It means that the variable y is also referencing the same object not the variable x. This is called as Shared Reference.

del x

x = "Geeks"  # Now if assign another value to the variable x, y is still referencing the same object with value 5.

y = "Computers"  # If we now assign a new value to y. The reference for the variable is now updated.

# The original object with value 5 is now eligible for the garbage.

# We can delete any variable using del keyword


# Practical Example
# Swapping Two variables

one, two = 5, 10
one, two = two, one

print(one)
print(two)


# Counting Characters in a String

word = "Python"
length = len(word)
print("Length of the word:", length)
