# -*- coding: utf-8 -*-
"""
1. object-oriented concept.
2. encapsulation (the most important oop concept)

ref:
https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/
https://softwareengineering.stackexchange.com/questions/336717/demonstrate-object-oriented-principles-to-non-programmers-using-physical-props
"""


class Temp:
    def __init__(self):
        pass


instance1 = Temp()


class Smartphone:
    def __init__(self, brand, model, **options):
        # these are Smartphone attributes.
        self.brand = brand
        self.model = model
        self._is_on = False
        self._battery = 100

    def turn_on(self):
        print('Turning on')
        if self._battery <= 20:
            self._low_battery()

        self._is_on = True

    def turn_off(self):
        print('Turning off')
        self._is_on = False

    def charge(self):
        print('Charging')
        self._battery = 100

    def _low_battery(self):
        print('Battery Low')


# iphone is an object or instance of Smartphone class.
iphone = Smartphone('iPhone', '8')
samsung = Smartphone('Samsung', 'S20')
result1 = isinstance(iphone, Smartphone)
result2 = isinstance(samsung, Smartphone)

if iphone.brand != samsung.brand:
    print('Different Brand')


if iphone.model != samsung.model:
    print('Different Model')

iphone.turn_on()
iphone.charge()
iphone.turn_off()
