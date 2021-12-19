# -*- coding: utf-8 -*-
"""
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


class smartphone:
    def __init__(self, brand, model):
        self._charge = 20
        self._power_on = False
        self._charge_per_minute = 0
        self._usage_per_minute = 0
        self._brand = brand
        self._model = model

    def check_minutes(self, num):
        if num <= 0:
            raise Exception('Invalid number of minutes')

    def charge(self, minutes):
        self.check_minutes(minutes)
        if self._charge < 100:
            charged = round(minutes * self._charge_per_minute)
            self._charge = min(self._charge + charged, 100)
            message = 'Charged for {minutes} minutes. The battery level is {charge_level}%'
            print(message.format(minutes=minutes, charge_level=self._charge))
        else:
            print('The phone is already fully charged')

    def play(self, minutes):
        self.check_minutes(minutes)
        if not self._power_on:
            print('The phone is off')
        else:
            used_charge = round(minutes * self._usage_per_minute)
            if self._charge <= used_charge:
                self._charge = 0
                self._power_on = False
                message = 'Battery is not sufficient to play for {minutes} minutes. Please charge your phone'
                print(message.format(minutes=minutes))
            else:
                self._charge = self._charge - used_charge
                message = 'Music is playing for {minutes} minutes, the new battery level is {charge_level}%'
                print(message.format(minutes=minutes, charge_level=self._charge))

    def turn_on(self):
        if not self._power_on:
            self._power_on = True
            message = 'The phone is turning on, battery level is {charge_level}%'
            print(message.format(charge_level=self._charge))
        else:
            print('The phone is already on')

    def turn_off(self):
        if self._power_on:
            print('The phone is turning off')
            self._power_on = False
        else:
            print('The phone is already off')

    def get_charge(self):
        if self._power_on:
            message = 'The battery level is {charge_level}%'
            print(message.format(charge_level=self._charge))
        else:
            print('The phone is off: charge level unknown')

    def get_brand(self):
        message = 'The phones brand is {brand}'
        print(message.format(brand=self._brand))

    def get_model(self):
        message = 'The phones model is {brand}'
        print(message.format(brand=self._model))


class samsung(smartphone):
    def brand_charge(self):
        self._charge_per_minute = round(20/20, 2)

    def brand_usage(self):
        self._usage_per_minute = round(10/20, 2)

    def charge(self, minutes):
        self.brand_charge()
        super().charge(minutes)

    def play(self, minutes):
        self.brand_usage()
        super().play(minutes)


class iphone(smartphone):
    def brand_charge(self):
        self._charge_per_minute = round(10/15, 2)

    def brand_usage(self):
        self._usage_per_minute = round(15/20, 2)

    def charge(self, minutes):
        self.brand_charge()
        super().charge(minutes)

    def play(self, minutes):
        self.brand_usage()
        super().play(minutes)


class oneplus(smartphone):
    def brand_charge(self):
        self._charge_per_minute = round(25/30, 2)

    def brand_usage(self):
        self._usage_per_minute = round(15/25, 2)

    def charge(self, minutes):
        self.brand_charge()
        super().charge(minutes)

    def play(self, minutes):
        self.brand_usage()
        super().play(minutes)

phone1 = oneplus('onePlus', '10Plus')
phone1.get_brand()
phone1.get_model()
phone1.turn_off()
phone1.turn_on()
phone1.charge(10)
phone1.get_charge()
phone1.play(2)
phone1.get_charge()
phone1.play(10)
phone1.play(20)

phone2 = samsung('Samsung', 'Galaxy')
phone2.get_brand()
phone2.get_model()
phone2.turn_off()
phone2.turn_on()
phone2.charge(10)
phone2.get_charge()
phone2.play(2)
phone2.get_charge()
phone2.play(10)
phone2.play(20)

