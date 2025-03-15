from collections import OrderedDict

"""OrderedDict in Python"""

"""
Ordered dictionary maintains the order of the key 
while regular dictionary does not gurantee the order of the key.
"""

# Basic Example :
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4

print("This is regular dictionary: \n")
for key, value in d.items():
    print(f"{key} {value}")

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4

print("This is Ordered Dictionary : \n")
for key, value in od.items():
    print(f"{key} {value}")


""" 1. Key value Change in Python Dictionary Order """

print("\nBefore : \n")
for key, value in od.items():
    print(f"{key} {value}")

print("\nAfter : \n")
od["c"] = 5
for key, value in od.items():
    print(key, value)


""" 2. Equality Comparison in Python Dictionary Order """
od1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od2 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

print("With keys in same order : od1 is od2 : ", od1 is od2)
print("With keys in same order : od1 == od2 : ", od1 == od2)


od1 = OrderedDict([("a", 1), ("c", 2), ("b", 3)])
od2 = OrderedDict([("c", 1), ("a", 2), ("b", 3)])

print("With keys in different order : od1 is od2 : ", od1 is od2)
print("With keys in different order : od1 == od2 : ", od1 == od2)


""" 3. OrderedDict Reversal in Python Dictionary Order """

reversed_dict = OrderedDict(reversed(list(od1.items())))
for key, value in reversed_dict.items():
    print(f"{key} {value}")


""" 4. OrderedDict Popitem() in Python Dictionary Order """

first_item = od1.popitem(
    last=False
)  # if last=True, will remove the last key and return it otherwise first key
print(first_item)

for key, value in od1.items():
    print(key, " ", value)


""" 4. Key Insertion at Arbitrary Position in Python Dictionary Ordered """
odi = OrderedDict([("a", 1), ("b", 2), ("c", 2), ("d", 4)])

odi.move_to_end("b")  # will move the key 'b' to the end
odi.move_to_end("d", last=False)  # will move the key 'd' to the first as last = False
print("After moving the keys : \n")
for key, value in odi.items():
    print(key, " ", value)


""" 5. Deletion and Re-Inserting in Python Dictionary Ordered """
odi.pop("c")
print("After deleting 'c' : \n")
for key, value in odi.items():
    print(f"{key} {value}")

odi["c"] = 3
print("After inserting the key 'c' again : \n")
for key, value in odi.items():
    print(f"{key} {value}")


""" 6. Collections Module in Python Dictionary Order """
odi.update([("e", 5), ("f", 6)])
odi.move_to_end("e", last=False)

for key, value in odi.items():
    print(f"{key} {value}")
