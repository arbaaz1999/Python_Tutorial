"""Loops in Python – For, While and Nested Loops"""

""" 1. Python While Loop """

count = 0
while count < 3:
    print("Hello Geeks")
    count += 1

""" 2. Infinite while Loop in Python : 
age = 28
while age > 19:
    print("Infinite Loop") """

""" 3. while loop with continue statement """
i = 0
s = "geeksforgeeks"
while i < len(s):
    if s[i] == "e" or s[i] == "s":
        i += 1
        continue
    print(s[i])
    i += 1


""" 4. while loop with break statement """
i = 0
s = "geeksforgeeks"
while i < len(s):
    if s[i] == "e" or s[i] == "s":
        i += 1
        break
    print(s[i])
    i += 1

""" 5. while loop with pass statement """
# An empty loop
a = "geeksforgeeks"
i = 0

while i < len(a):
    i += 1
    pass

print("Value of i :", i)

""" 6. while loop with else """
i = 0
s = "geeksforgeeks"
while i < len(s):
    i += 1
    print(i)
else:
    print("Else condition executed", s)


i = 0
s = "geeksforgeeks"
while i < len(s):
    i += 1
    print(i)
    if i >= 4:
        print("While loop terminated, No else condition executed")
        break
else:
    print("Else condition executed", s)
