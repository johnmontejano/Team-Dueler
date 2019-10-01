import random
import pytest
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print('woof!!!')

my_dogs = list()

my_dogs.append(Dog('james', 'husky'))
my_dogs.append(Dog('james', 'pitbull'))

for dog in my_dogs:
    dog.bark()

    def sit(self):
        print('Sit now!')
    def roll_over(self):
        print('roll!')
