# -*- coding: utf-8 -*-
"""
1. abstraction.
2. inheritance.
3. polymorphism.
"""

# ENCAPSULATION:

# ABSTRACTION:

# INHERITANCE:
# attributes are: specifications
# methods are: behaviors

# POLYMORPHISM:


class Animal:
    def __init__(self, name):
        self._energy = 50
        self._name = name
        self._age = 0
        self._is_hungry = True

    def eat(self, food):
        print('{name} is eating {food}.'.format(food=food, name=self._name))
        self._is_hungry = False
        self._energy = self._energy + 1

    def scare(self):
        print('{name} is scared.'.format(name=self._name))
        self._move()

    def make_sound(self):
        raise Exception('I dont know how to make sound')

    def _move(self):
        print('{name} is moving.'.format(name=self._name))
        self._is_hungry = True
        self._energy = self._energy - 1


class Dog(Animal):
    def make_sound(self):
        print('Dog is barking.')

    def _move(self):
        super()._move()
        self._energy = self._energy - 1


class Husky(Dog):

    def eat(self, food):
        super().eat(food)
        self._energy = self._energy + 1

    def _move(self):
        super()._move()
        self._energy = self._energy - 1



class Frog(Animal):
    def make_sound(self):
        print('Frog is Ghooring.')

    def _jump(self):
        print('Frog is jumping.')

    def scare(self):
        print('Frog is scared.')
        self._jump()


class Snake(Animal):
    def _sting(self):
        print('Snake is stinging.')

    def scare(self):
        print('Snake is scared.')
        self._sting()

    def eat(self, food):
        if food != 'meat':
            print('Snake does not eat but meat.')
            return

        super().eat(food)

    def make_sound(self):
        pass


noah = Animal('Noah')
dog1 = Dog('Rex')
dog2 = Dog('Jordan')
husky = Husky('White Teeth')
frog = Frog('Aunt')
snake = Snake('Ghashghash')

##noah.make_sound()
dog1.make_sound()
husky.make_sound()
snake.scare()
frog.scare()

print('POLYMORPHISM')
animals = [dog2, dog1, husky, frog, snake]
for item in animals:
    if isinstance(item, Animal):
        item.scare()
        item.eat('Bread')
        item.eat('meat')
        item.make_sound()
