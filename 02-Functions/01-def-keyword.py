"""Python def Keyword"""


# defining function


def func():
    print("This is the first function!")


# calling function
func()


""" 1. Python def Syntax """

"""
def function_name () :
    function definition

    return expression
"""

""" 2. Passing Function as an Argument """


def fun(func, arg):
    return func(arg)


def square(x):
    return x**2


res = fun(square, 5)
print(res)


""" 3. Python def keyword example with *args """


def fun(*args):
    print("Arguments passed to this function are : ")
    for arg in args:
        print(arg)


fun(1, 2, 3)


""" 4. Python def keyword example with **kwargs """


def fun(**kwargs):
    print("Key=Value Arguments Passed to this function are :")
    for key, value in kwargs.items():
        print(f"key={key} and value={value}")


fun(firstName="Arbaaz", lastName="Mansuri")


""" 5. Python def keyword example with the class """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hurray! {self.name} turns {self.age} today!")


p1 = Person("Arbaaz", 24)
p1.greet()
