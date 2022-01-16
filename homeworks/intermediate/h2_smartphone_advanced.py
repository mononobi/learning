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
    def __init__(self, brand, model):
        self._charge = 20
        self._power_on = False
        self._charge_per_minute = 0
        self._usage_per_minute = 0
        self._brand = brand
        self._model = model

    @property
    def charge(self):
        self._charge

    @property
    def power_on(self):
        self._power_on

    @charge_per_minute.setter
    def charge_per_minute(self, value):
        utils.assert_positive_number(value)
        if value > 100:
            raise Exception('Change more than 100 invalid')
        else:
            self._charge_per_minute = value

    @usage_per_minute.setter
    def usage_per_minute(self, value):
        utils.assert_positive_number(value)
        if value > 100:
            raise Exception('Change more than 100 invalid')
        else:
            self._usage_per_minute = value

    @staticmethod
    def get_brand():
        pass

    @staticmethod
    def get_model():
        pass

    def charge(self, minutes):
        ##utils.assert_positive_number(minutes)
        charged = round(minutes * self._charge_per_minute)
        self._charge = min(self._charge + charged, 100)
        message = 'Charged for {minutes} minutes. The battery level is {charge_level}%'
        return self._charge

    def play(self, minutes):
        ##utils.assert_positive_number(minutes)
        if not self._power_on:
            raise Exception('The phone is off')
        else:
            used_charge = round(minutes * self._usage_per_minute)
            if self._charge <= used_charge:
                self._charge = 0
                self._power_on = False
                raise Exception('Battery not sufficient')
            else:
                self._charge = self._charge - used_charge
                return self._charge

    def turn_on(self):
        if not self._power_on:
            self._power_on = True
        else:
            raise Exception('The phone is already on')

    def turn_off(self):
        if self._power_on:
            self._power_on = False
        else:
            raise Exception('The phone is already off')

    def get_charge(self):
        if self._power_on:
            return self._charge
        else:
            raise Exception('The phone is off')





class Samsung(Smartphone):
    def __init__(self, model):
        super().__init__('Samsung', model) ##???
        #self._charge_per_minute = round(20/20, 2)
        #self._usage_per_minute = round(10/20, 2)

    charge_per_minute = round(20/20, 2)
    usage_per_minute = round(10 / 20, 2)

    @staticmethod
    def get_brand():
        return 'Samsung'

    @staticmethod
    def get_model():
        pass


class iPhone(Smartphone):
    def __init__(self, model):
        super().__init__('iPhone', model) ##???
        #self._charge_per_minute = round(10/15, 2)
        #self._usage_per_minute = round(15/20, 2)

    charge_per_minute = round(10/15, 2)
    usage_per_minute = round(15/20, 2)

    @staticmethod
    def get_brand():
        return 'iPhone'

    @staticmethod
    def get_model():
        pass

class OnePlus(Smartphone):
    def __init__(self, model):
        super().__init__('iPhone', model) ###??
        #self._charge_per_minute = round(25/30, 2)
        #self._usage_per_minute = round(15/25, 2)

    charge_per_minute = round(25 / 30, 2)
    usage_per_minute = round(15 / 25, 2)

    @staticmethod
    def get_brand():
        return 'OnePlus'

    @staticmethod
    def get_model():
        pass ##??