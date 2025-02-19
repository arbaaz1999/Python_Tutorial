"""Python return statement"""


# Example
def add(a, b):
    return a + b


sum = add(5, 6)
print("Add function : ", sum)


def is_true(a):
    return bool(a)


res = is_true(2 < 5)
print("is 2 less than 5 : ", res)


""" 1. Syntax """
"""
def function_name(parameters):
    
    function_body
    
    return value
"""


""" 2. Returning Multiple Values """


def fun():
    name = "Alice"
    age = "24"
    return name, age


name, age = fun()
print(f"Name -> {name} and Age -> {age}")


""" 3. Returning List """


def fun(n):
    return [n**2, n**3]


series = fun(2)
print("Series : ", series)


""" 4. Function returning another function """


def fun1(msg):
    def fun2():
        return f"Message {msg}"

    return fun2


string = fun1("Hello World")

print(string())


""" 5. Multiple return statement """


def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


print(check_number(5))
print(check_number(-3))
print(check_number(0))
