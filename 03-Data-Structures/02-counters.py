"""Python collections Counter | Set 1"""

from collections import Counter

# Basic Example :

ctr1 = Counter([1, 2, 2, 3])  # creating counter with iterable
ctr2 = Counter([2, 3, 3, 4])

ctr3 = Counter({1: 1, 2: 3, 3: 4})  # creating counter with dictionary

ctr4 = Counter("hello world")  # creating a counter from a string


# accessing the elements of counter
print(ctr1[1])
print(ctr1[2])
print(ctr1[3])
print(ctr1[4])

#  updating a counter
ctr1.update([1, 2, 3, 4, 5])

# counter element() method
items = list(ctr1.elements())
print(items)

# counter most_common(n) method
common = ctr1.most_common(1)
print(common)

# counter substract() method
ctr1.subtract("world")


# Arithmetic operations on Counter
new_ctr = ctr1 + ctr2  # addition
print("Addition : ", new_ctr)


print(ctr1)
print(ctr2)
print(ctr3)
print(ctr4)


"""Counters in Python | Set 2"""

# A counter never throw a KeyValueError, let's understand with below example
# Create a list
z = ["blue", "red", "blue", "yellow", "blue", "red"]
col_count = Counter(z)
print(col_count)

colours = ["blue", "red", "yellow", "green"]  # key 'green' is not there in col_count

for col in colours:
    print(
        col, col_count[col]
    )  # output for the frequency of green will 0 and it will not throw any error


""" elements() method of Counter in Python """

coun = Counter(a=1, b=3, c=2, d=0)
print(coun)

coun_elem = list(coun.elements())
print(coun_elem)  # noticed that the element with 0 value will not be included


"""most_common() method of Counter in Python"""

coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

print(coun.most_common(3))

for letter, count in coun.most_common(3):
    print(f"{letter} {count}")
