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



import homeworks.intermediate.utils as utils

class Smartphone:
    def __init__(self, brand, model, charge_per_minute, usage_per_minute):
        utils.assert_positive_number(charge_per_minute)
        if charge_per_minute > 100:
            raise Exception('Change more than 100 invalid')
        utils.assert_positive_number(usage_per_minute)
        if usage_per_minute > 100:
            raise Exception('Change more than 100 invalid')
        self._charge = 20
        self._is_powered_on = False
        self.__charge_per_minute = charge_per_minute
        self.__usage_per_minute = usage_per_minute
        self._brand = brand
        self._model = model

    @property
    def get_charge(self): ## Properties normaly start with get or is or has ...
        if not self._is_powered_on:
            raise Exception('The phone is off')
        return self._charge ## property MUST return a variable

    @property
    def is_powered_on(self):
        return self._is_powered_on

    @property
    def charge_per_minute(self):
        return self.__charge_per_minute

    @property
    def usage_per_minute(self):
        return self.__usage_per_minute

    def get_brand(self):  ## it is better not define it static. because it is not possible, for BRAND is an input
        ##pass
        return self._brand

    def get_model(self):  ## same explanation as get_brand
        ##pass
        return self._model

    def charge(self, minutes):
        utils.assert_positive_number(minutes)
        charged = round(minutes * self.__charge_per_minute)
        self._charge = min(self._charge + charged, 100)
        return self._charge

    def play(self, minutes):
        utils.assert_positive_number(minutes)
        if not self._is_powered_on:
            raise Exception('The phone is off')
        used_charge = round(minutes * self.__usage_per_minute)
        if self._charge <= used_charge:
            self._charge = 0
            self._is_powered_on = False
            raise Exception('Battery not sufficient')
        self._charge = self._charge - used_charge
        return self._charge

    def turn_on(self):
        if not self._is_powered_on:
            self._is_powered_on = True
        raise Exception('The phone is already on')

    def turn_off(self):
        if not self._is_powered_on:
            raise Exception('The phone is already off')
        self._is_powered_on = False


class Samsung(Smartphone):
    def __init__(self, model):
        super().__init__('Samsung', model, round(20/20, 2), round(10/20, 2))
        #self._charge_per_minute = round(20/20, 2)
        #self._usage_per_minute = round(10/20, 2)


class iPhone(Smartphone):
    def __init__(self, model):
        super().__init__('iPhone', model, round(10/15, 2), round(15/20, 2))
        ##self._charge_per_minute = round(10/15, 2)
        ##self._usage_per_minute = round(15/20, 2)


class OnePlus(Smartphone):
    def __init__(self, model):
        super().__init__('OnePlus', model, round(25/30, 2), round(15/25, 2))
        ##self._charge_per_minute = round(25/30, 2)
        ##self._usage_per_minute = round(15/25, 2)
