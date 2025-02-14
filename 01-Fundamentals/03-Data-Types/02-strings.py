# String Data Type :
# 1. String
# a. Creating a String:
s1 = "GfG"  # using single quote ('')
s2 = "GfG"  # using double quotes ("")
print(s1)
print(s2)

# b. Multi-line Strings:
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)  # using three double quotes (""" """)

s = """I'm a 
Geek"""
print(s)  # using three single quotes (''' ''')

# c. Accessing characters in Python String
s = "GeeksforGeeks"
# Accesses first character: 'G'
print(s[0])
# Accesses 5th character: 's'
print(s[3])

# d. Access string with Negative Indexing
s = "GeeksforGeeks"
# Accesses last character s'
print(s[-1])
# Accesses 5th character from end: 'G'
print(s[-5])

# e. String Slicing
s = "Geeks For Geeks"
print("From Index 1 to 3", s[1:4])

print("From Index 0 to 4", s[:5])

print("From Index 5 to length of string", s[5:])

print("String Reversed : ", s[::-1])

# e. String Immutability
s = "geeksforgeeks"
s = "G" + s[1:]
print(s)

# f. Deleting a String
s = "GFG"
del s


# f. Updating a String
s = "geeksforgeeks"
s2 = s.replace("g", "G")
print("g replace with G : ", s2)


# g. Common String Methods
s = "geeksforgeeks"
s2 = "HELLO WORLD"
length = len(s)  # gives the length of the string

print(s.upper())  # GEEKSFORGEEKS
print(s2.lower())  # hello world


s = "      Gfg      "
print(s.strip())  # removes leading and trailing space from the string

s = "Python is Fun"
print(s.replace("Fun", "Awesome"))  # replace the first parameter with the second one


# h. Concatenating and Repeating Strings
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # Concatenating multiple strings using + operator

s = "hello "
print(s * 3)  # repeats string 3 times using * asterisk


# i. Formatting String
# a. Using f-string
name = "Arbaaz"
age = "25"
print(f"My name is {name} and my age is {age}")

# b. Using format() method
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)


# j. Using in for String Membership Testing
s1 = "geeksforgeeks"
print("geeks" in s1)
print("gfg" in s1)
