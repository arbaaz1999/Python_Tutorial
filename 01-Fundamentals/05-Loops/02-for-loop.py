"""Loops in Python – For, While and Nested Loops"""

""" 1. Python For Loops """

s = ["Geeks", "for", "Geeks"]

# using for loop with string
for i in s:
    print(i)

""" 2. Python For Loop with String """
s = "GeeksforGeeks"
for i in s:
    print(i, end=" ")

print("\n")

""" 3. Using range() with For Loop """
for i in range(1, 11):  # range(start, stop, step)
    print(3 * i)


""" 4. Continue with For Loop """
for i in range(0, 10):
    if i == 5 or i == 7:
        continue
    print(i, end=" ")

print("\n")

""" 5. Break with For Loop """
for i in range(0, 10):
    if i == 8:
        break
    print(i, end=" ")

""" 6. Pass Statement with For Loop """
# An empty loop
for i in "geeksforgeeks":
    pass
print(i)

""" 7. Else Statement with For Loops """
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

""" 8. Using Enumerate with for loop """
li = ["apple", "mango", "banana", "orange"]
for i, j in enumerate(li):
    print(f"{j} at {i} position")


""" 9. Nested For Loops in Python """
for i in range(0, 5):
    for j in range(i):
        print("*", end=" ")
    print(" ")
