"""
Encapsulation in python works differently compared to Java (I guess!)
In python we use "_" and "__" for protected and private variables

Definition: Encapsulation is an ability to hide part of variables and its behaviors from outside the class

Important Links:
1. https://medium.com/@manjuladube/encapsulation-abstraction-35999b0a3911   (A good article)
2. https://www.askpython.com/python/oops/encapsulation-in-python
3. https://www.educative.io/edpresso/what-is-encapsulation-in-python (doesn't explain clearly)

"""


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("My name is {0} and I am {1} years young".format(self.name, self.age))


person = Person("Keerthi", 26)
print("********************************** from outside the class **********************************")
print("My name is {0} and I am {1} years young".format(person.name, person.age))
print("********************************** from inside the class **********************************")
person.display()


"""
Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses. 
How to accomplish this in Python? The answer is — by convention. By prefixing the name of your member with a 
single underscore, you’re telling others “don’t touch this, unless you’re a subclass”. See the example below:
refer: https://medium.com/@manjuladube/encapsulation-abstraction-35999b0a3911
"""


class Human():
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected using "_" some people dont like to reveal age :P

    def display(self):
        print("My name is {0} and I am {1} years young".format(self.name, self._age))


human = Human("Racheal", 46)
print("********************************** from outside the class **********************************")
print("My name is {0} and I am {1} years young".format(human.name, human._age))
print("********************************** from inside the class **********************************")
human.display()



class Hooman():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private using "__" some people dont like to reveal age :P

    def display(self):
        print("My name is {0} and I am {1} years young".format(self.name, self.__age))


homan = Hooman("Ross", 51)
print("********************************** from inside the class **********************************")
homan.display()
print("********************************** from outside the class **********************************")
print("My name is {0} and I am {1} years young".format(homan.name, homan.__age))



"""
********************************** from outside the class **********************************
My name is Keerthi and I am 26 years young
********************************** from inside the class **********************************
My name is Keerthi and I am 26 years young
********************************** from outside the class **********************************
My name is Racheal and I am 46 years young
********************************** from inside the class **********************************
My name is Racheal and I am 46 years young
********************************** from inside the class **********************************
My name is Ross and I am 51 years young
********************************** from outside the class **********************************
Traceback (most recent call last):
  File "/Users/keerthi/Desktop/projects/ObjectOrientedDesign/encapsulation.py", line 69, in <module>
    print("My name is {0} and I am {1} years young".format(homan.name, homan.__age))
AttributeError: 'Hooman' object has no attribute '__age'
"""