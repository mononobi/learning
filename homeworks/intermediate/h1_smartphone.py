# -*- coding: utf-8 -*-
"""
we want to have a base smartphone class and an unlimited concrete smartphones.
any smart phone should have these common interfaces:

1. turn_on: turns the phone on.
2. turn_off: turns the phone off.
3. charge: start charging the phone for specified minutes.
4. get_charge: show the battery percentage.
5. play: play with the phone for specified minutes.
6. brand: show the phone's brand (.ex iPhone, Samsung, ...)
7. model: show the phone's model (.ex SE, Galaxy S20, 9, ...)

when a smartphone is created it should have 20% initial charge and it is turned off.

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

Make different smartphone classes and make instances of each one and use
the common interface to interact with each phone.
"""
