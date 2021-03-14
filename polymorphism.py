"""
“Poly­mor­phism is the abil­i­ty of a pro­gram to detect the real class of an object and call its
implementation even when its real type is unknown in the cur­rent context.”

Excerpt From: Alexander Shvets. “Dive Into Design Patterns.” Apple Books.

"""




class Animal():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.type = type

    def breathe(self):
        print(self.type+" is breathing")

    def eat(self):
        print("I eat {0} food".format(self.type))

class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def talk(self):
        print("I barks")


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def talk(self):
        print("Meow Meow")


cat1 = Cat("Kitty", 2.5, "male")
dog1 = Dog("Fluffy", 4, "male")

for animal in (cat1, dog1):
    animal.talk()
