# -*- coding: utf-8 -*-
"""
Redo the following application with access levels and other attribute
types (instance methods, static methods, properties, attributes) in mind:

we want to have a base smartphone class and an unlimited concrete smartphones.
any smartphone should have these common interfaces:

1. turn_on: turns the phone on.
2. turn_off: turns the phone off.
3. charge: starts charging the phone for specified minutes.
4. get_charge: shows the battery percentage.
5. play: plays with the phone for specified minutes.
6. brand: shows the phone's brand (.ex iPhone, Samsung, ...)
7. model: shows the phone's model (.ex SE, Galaxy S20, 9, ...)

when a smartphone is created it should have 20% initial charge, and it is turned off.

the `charge()` method must get a value as minutes of charging.
different types of smartphones get charged at different rates:

- Samsung smartphones get 20% of charge after 20 minutes of charging.
- iPhones get 10% of charge after 15 minutes of charging.
- OnePlus smartphones get 25% of charge after 30 minutes of charging.

the `play()` method must get a value as minutes of playing.
different types of smartphones lose charge at different rates:

- Samsung smartphones lose 10% of charge after 20 minutes of playing.
- iPhones lose 15% of charge after 20 minutes of playing.
- OnePlus smartphones lose 15% of charge after 25 minutes of playing.

* when a phone's charge reaches to 0, it must be turned-off.
* when charging a phone, the battery percentage should not go over 100.

Make different smartphone classes and make instances of each one and use
the common interface to interact with each phone.
"""

from abc import ABC

class Smartphone:
    """"A class to define general attributes and methods for a modern smartphone."""

    # Let's see how many smartphones is built in the program:
    count_of_smartphone_models = 0

    def __init__(self, brand, model):
        """Any concrete smartphone is created in turned off mode with 20% charge."""

        self._brand = brand
        self._model = model
        self._power_mode = False
        # In percentage:
        self._battery_charge = 20

        Smartphone.count_of_smartphone_models += 1

    # Q: Should these super methods be "protected"?
    def turn_on(self):
        if not self._power_mode:
            self._power_mode = True
            print(f'Turning {self._brand} on.')
        else:
            print('Already on.')

    def turn_off(self):
        if self._power_mode:
            self._power_mode = False
            print(f'Turning {self._brand} off.')
        else:
            print('Already off.')

    def _charge(self, minutes):
        print(f'Charging for {minutes} minutes.')
        if self._battery_charge > 100:
            self._battery_charge = 100

    def get_charge(self):
        print(f'This {self._brand} has {self._battery_charge}% charge.')

    def _play(self, minutes):
        print(f'Playing for {minutes} minutes.')
        if self._battery_charge <= 0:
            self._battery_charge = 0
            self.turn_off()

    @property
    def brand(self):
        return self._brand

    def show_brand(self):
        print(f'This is {self._brand} smartphone.')

    def model(self):
        print(f'This is {self._model} smartphone.')

    # For charge or discharge
    @staticmethod
    def calculate_charge(a, b):
        return round(a * b)


class Samsung(Smartphone):
    """Specific smartphone that has behavior in charging and playing"""

    def __init__(self, model):
        super().__init__('Samsung', model)
        self.__charging_rate = 1
        self.__usage_rate = 0.5

    # Q: Should it be charge or _charge?
    def charge(self, minutes):
        self._battery_charge += Smartphone.calculate_charge(minutes, self.__charging_rate)
        # Before static method: round(minutes * self.__charging_rate)
        super()._charge(minutes)
        print(f'{self._brand} is being charged to {self._battery_charge}%')

    def play(self, minutes):
        self._battery_charge -= Smartphone.calculate_charge(minutes, self.__usage_rate)
        super()._play(minutes)
        print(f'{self._brand} is decharged to {self._battery_charge}%')


class Iphone(Smartphone):
    """Specific smartphone that has behavior in charging and playing"""

    def __init__(self, model):
        super().__init__('Iphone', model)
        self._charging_rate = 0.67
        self._usage_rate = 0.75

    def charge(self, minutes):
        self._battery_charge += Smartphone.calculate_charge(minutes, self._charging_rate)
        super()._charge(minutes)
        print(f'{self._brand} is being charged to {self._battery_charge}%')

    def play(self, minutes):
        self._battery_charge -= Smartphone.calculate_charge(minutes, self._usage_rate)
        super()._play(minutes)
        print(f'{self._brand} is decharged to {self._battery_charge}%')


class Oneplus(Smartphone):
    """Specific smartphone that has behavior in charging and playing"""

    def __init__(self, model):
        super().__init__('Oneplus', model)
        self._charging_rate = 0.83
        self._usage_rate = 0.6

    def charge(self, minutes):
        self._battery_charge += Smartphone.calculate_charge(minutes, self._charging_rate)
        super()._charge(minutes)
        print(f'{self._brand} is being charged to {self._battery_charge}%')

    def play(self, minutes):
        self._battery_charge -= Smartphone.calculate_charge(minutes, self._usage_rate)
        super()._play(minutes)
        print(f'{self._brand} is decharged to {self._battery_charge}%')


# Demonstrate:

phones = [Samsung('S10'), Iphone('13'), Oneplus('aa')]

for phone in phones:
    phone.show_brand()
    phone.model()
    phone.turn_on()
    phone.get_charge()
    phone.charge(30)
    phone.charge(1000)
    phone.play(20)
    phone.play(100)
    phone.play(1000)
    phone.get_charge()
    phone.turn_off()
    print('\n')

print(Smartphone.count_of_smartphone_models)


# phone1 = Smartphone('samsung', 's10')
# phone1.turn_on()
# phone1.get_charge()
# phone1.charge(10)
# phone1.get_charge()
# phone1.turn_off()
# print('\n')