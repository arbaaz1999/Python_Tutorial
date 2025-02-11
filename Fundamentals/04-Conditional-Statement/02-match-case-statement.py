"""Python Match Case Statement"""


# 1. Basic Example
def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")


check_number(10)
check_number(30)


# 2. Match Case Statements with Constants
def greet(person):
    match person:
        case "A":
            print("Hello, A!")
        case "B":
            print("Hello, B!")
        case _:
            print("Hello, stranger!")


greet("A")
greet("B")


# 3. Match Case Statement with OR Operator
def num_check(x):
    match x:
        case 10 | 20 | 30:  # Matches 10, 20, or 30
            print(f"Matched: {x}")
        case _:
            print("No match found")


num_check(10)
num_check(20)
num_check(25)


# 4. Match Case Statement with Python If Condition
def num_check(x):
    match x:
        case 10 if x % 2 == 0:  # Match 10 only if it's even
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found")


num_check(10)
num_check(15)


# 5. Match Case Statement on Sequences
def process(data):
    match data:
        case [x, y]:
            # A list with two elements
            print(f"Two-element list: {x}, {y}")
        case [x, y, z]:
            # A list with three elements
            print(f"Three-element list: {x}, {y}, {z}")
        case _:
            print("Unknown data format")


process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])


# 6. Match Case Statement on Mappings (Dictionaries)
def person(person):
    match person:
        # Dictionary with name and age keys
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")

        # Dictionary with only name key
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")


person({"name": "Alice", "age": 25})
person({"name": "Bob"})
person({"city": "New York"})


# 7. Match Case Statement with Python Class
class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


def check_shape(shape):
    match shape:
        # Match Circle and extract the radius
        case Circle(radius):
            print(f"circle radius {radius}.")

        # Match Rectangle and extract width and height
        case Rectangle(width, height):
            print(f"Rectangle width {width} and height {height}.")

        # Default case for any other object
        case _:
            print("This is an unknown shape.")


# Create objects of Circle and Rectangle
circle = Circle(10)
rectangle = Rectangle(4, 6)

# Test with different shapes
check_shape(circle)
check_shape(rectangle)

"""
Explanation:
- We have a Shape class and two types of shapes: Circle and Rectangle.
- The check_shape function checks if the shape is a Circle or Rectangle and prints their details.
- If the shape isn’t one of these, it says “unknown shape.”
"""
