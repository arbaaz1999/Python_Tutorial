"""Python Classes and Objects"""

""" 1. Create a Class """


# define a class
class Dog:
    sound = "bark"  # class attribute


# create an object from the class
dog1 = Dog()

# access the class attribute
print("Class attribute : ", dog1.sound)


""" 2. Using __init__() Function """


class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


""" 3. Initiate Object with __init__ """

dog2 = Dog("Modi", 75)
print("Class Attribute : ", dog2.species)
print("Instance Attribute : ", dog2.name)


""" 4. Self Parameter """
# is a reference to the current instance of the class.


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")


dog3 = Dog("Modiv2", 75)
dog3.bark()


""" 5. __str__ Method """
# allows to define a custom string representation of an object.


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


"""   def __str__(self):
    return f"{self.name} is {self.age} years old!"  # Correct: Returning a string """


dog1 = Dog("Hola", 5)
dog2 = Dog("Bhola", 6)
print(dog1)
print(dog2)

# if we not define the __str__ method then the instance of a class will return a string like this e.g. <__main__.Dog object at 0x000001D7DD9A6E40>


""" 6. Class and Instance Variables in Python """
# Class Variables : These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Variables : Variables that are unique to each instance (object) of a class. These are defined within __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.


# Example :
class Dog:
    # class/static variable
    species = "Canine"

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age


dog1 = Dog("buddy", 4)
dog2 = Dog("charlie", 5)

# access class variable
print("Accessing class variable : ", Dog.species)

# modifying class variable
Dog.species = "Feline"
print("Accessing class variable after modification : ", Dog.species)
