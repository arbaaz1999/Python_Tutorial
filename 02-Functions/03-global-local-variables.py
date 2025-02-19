"""Global and Local Variables in Python"""

""" 1. Python Local Variables """


# a. Creating local variables in Python
def f():
    # local variable
    s = "I love Geeksforgeeks"
    print(s)


# Driver code
f()


# b. Can we access local variable outside the function
def f():
    # local variable
    s = "This is local variable"
    print(s)


f()
# print(s) Will throw NameError: name 's' is not defined


""" 2. Python Global Variables """

# a. Create a global variable  in Python


def fun():
    print("Inside Function", s)


# global variable
s = "This is global variable"
fun()
print("Outside function : ", s)


""" 3. The global Keyword """

s = "Python is Great!"


def f():
    global s
    s += " GFG!"
    print("Changed inside function using global keyword : ", s)
    s = "Than changed locally"
    print(s)


print("Before function call : ", s)
f()
