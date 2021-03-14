"""
duck-typing   A programming style which does not look at an object’s type to determine if it has the right interface;
instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck,
it must be a duck.”) By emphasizing interfaces rather than specific types,
well-designed code improves its flexibility by allowing polymorphic substitution.
"""


"""
hasattr(object, name)
"""

# Example for hasattr


class Person:
    age = 26
    name = "Keerthi"


person = Person()
print("Person has age?:", hasattr(person, "age"))  # prints True
print("Person is married?:", hasattr(person, "marriage")) # prints False


"""
what is abstraction? 

abstraction is a model of a real word objects or phenomenon that only concentrates on the attributes that are applicable 
to current context and discards the rests. (not book definition, my own definition)

Abstraction: implementation Hiding
example: imagine we have a Airplane class in Airplane simulator and Airplane ticket booking application 
we have different attributes in Airplane simulator like lattitude, longitude, angle, turbos etc 
but in Airplane ticket app just mapping of seat number and availble seats. Hiding implementation from the user. :) 
"""

# ABC --> abstract base class and abstract methods
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.type = type

    def breathe(self):
        print(self.type+" is breathing")

    def eat(self):
        print("I eat {0} food".format(self.type))

    @abstractmethod
    def talk(self):
        pass


# animal = Animal()    # gives error, we cannot instantiate abstract method


class Dog(Animal):
    def __init__(self):
        super().__init__("Candy", 2, "female")

    def talk(self):
        print("I barks")


dog = Dog()
print("{0} is my name and I am {1} old".format(dog.name, dog.age))
dog.talk()

animal = Animal()