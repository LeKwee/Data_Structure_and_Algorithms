from abc import ABC, abstractmethod

class Animal(ABC):
    '''
    classes inheriting Animal MUST override func1 due to @abstractmethod
    '''
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        print('Woof')
        
class Cat(Animal):
    def sound(self):
        print('meow')


dog = Dog()
dog.makeSound()

cat = Cat()

'''
OUTPUT:

Woof
Traceback (most recent call last):
  File "abstract_class.py", line 23, in <module>
    cat = Cat()
TypeError: Can't instantiate abstract class Cat with abstract methods makeSound

'''