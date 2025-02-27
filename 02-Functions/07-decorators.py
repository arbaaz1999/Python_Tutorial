"""Decorators in Python"""


# Decorator Example :
# A simple decorator function :
def decorator(func):
    def wrapper(*args, **kwargs):
        print("One feature added before the existing function call")
        func(*args, **kwargs)
        print("One more feature added after the existing function call")

    return wrapper


@decorator
def greet():
    print("This is the existing functionality")


greet()


""" 1. Higher-Order Functions """


def fun(func, x):
    return func(x)


def square(x):
    return x**2


res = fun(square, 3)
print(res)


""" 2. Functions as First-Class Objects """


def greet(m):
    return f"Hello {m}"


say_hi = greet
print(say_hi("Bob"))


def apply(f, v):
    return f(v)


res = apply(say_hi, "Alice")
print(res)


def make_mult(f):
    def mult(x):
        return f * x

    return mult


dbl = make_mult(2)
print(dbl(5))


""" 3. Types of Decorators """
""" i. Function Decorators"""


def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@simple_decorator
def greet():
    print("Hello World")


greet()


""" ii. Method Decorators """


def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Befor method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res

    return wrapper


class MyClass:
    @method_decorator
    def say_hi(self):
        print("Hello")


obj = MyClass()
obj.say_hi()


""" iii. Class Decorators """


def fun(cls):
    cls.person_name = "Arbaaz"

    def say_hello():
        return f"Hello {cls.person_name}"

    cls.greet = say_hello

    return cls


@fun
class Person:
    pass


print(Person.person_name)
print(Person.greet())


""" 4. Common Built-in Decorators in Python """
