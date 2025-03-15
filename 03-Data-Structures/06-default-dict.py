from collections import defaultdict

"""Defaultdict in Python"""

# Basic Example :

# Here, int is a factory function that defines the default value. Each time a key is accessed that doesn’t exist, it will automatically be assigned an empty list.
d = defaultdict(int)
d["name"] = "Arbaaz"
print("Created empty default dict : ", d)
print("Key that does not exist : ", d["surname"])


""" 1. What is default factory in Python dict? """


# It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
d = defaultdict(lambda: "Not present")
d["a"] = 1
d["b"] = 2

print("Key is present : ", d["a"])
print("Key is present : ", d["b"])
print("Key is not present : ", d["c"])


""" 2. Python defaultdict Type for Handling Missing Keys """
print(d.__missing__("a"))
print(d.__missing__("c"))


"""
Like wise:
same for int,
same for str,
same for list,
and for any callable objects as default_factory.
"""
