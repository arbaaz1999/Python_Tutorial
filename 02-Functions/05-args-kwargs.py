"""*args and **kwargs in Python"""

"""
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
"""

""" 1. Python *args """


# Example 1 :
def fun(*argv):
    for arg in argv:
        print(arg)


fun("Hello", "Welcome", "to", "GeeksForGeeks")


# Example 2 :
def fun(arg1, *argv):
    print("First Argument : ", arg1)
    print("Rest of the Arguments are : ")
    for arg in argv:
        print(arg)


fun("First", "rest", "of", "the", "arguments", 1, 2, 3, 4, True, 2.56789)


""" 2. Python **kwargs """


# Example 1 :
def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k} = {val}")


fun(firstName="Arbaaz", lastName="Mansuri", age=25, isMale=True, heightInCm=175.5)


# Example 2 :
def fun(arg1, **kwargs):
    print("This is first argument : ", arg1)
    for k, val in kwargs.items():
        print(f"{k} = {val}")


fun("Hello", first="First", second="Second")


""" 3. Using both *args and **kwargs """


def fun(*args, **kwargs):
    print("Without Keyword Arguments : ", args)
    print("With Keyword Arguments ", kwargs)


fun(1, 2, 3, a=1, b=2, c=3)
