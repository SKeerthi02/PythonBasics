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


# animal = Animal()    # gives error, we cannot instantiate abstract method


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


dog = Dog("Candy", 2, "female")
print("{0} is my name and I am {1} old".format(dog.name, dog.age))
dog.talk()

# animal = Animal()
cat = Cat("Tom", 1, "male")
cat.talk()