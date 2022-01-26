# -*- coding: utf-8 -*-
"""
1. method access levels.
2. attribute access levels.
2. issubclass check.
3. static methods.
4. properties.
"""

# different access levels:
# public: child classes could override them and outer user could also call them.
# protected: child classes could override them but outer user should not call them.
# private: child classes should not override them and outer user should not call them.

# access levels help us achieve encapsulation.


class Car:

    def __init__(self):
        # Attributes:
        self.__km = 0
        self._model = None
        # self.rate = 5 public rate is not good because it can lead to wrong values.
        self._rate = 5

    def run(self):
        self.__km += 10

    def start(self):
        self._check()

    def brake(self):
        pass

    def _check(self):
        pass

    def __transmit(self):
        pass
    # for instance-method you need to build a object from the class and the call them
    # for staticmethods you do not need to build an oject from the class, you can directly call the methods from the classs itself
    # staticmethod has no SELF input variable
    @staticmethod
    def get_brand():
        pass

    # property is an attribute. They are written as methods
    # you cant call them
    # you can only handle them as attributes. WITHOUT a ()
    # its difference with attributes is that it garauntees Encpsulation
    @property
    def model(self):
        return self._model

    @property
    def rate(self):
        return self._rate
    # each Property is b default a GETTER (read only)
    # if you want the property to be editable from outside, you should define it as a STTER
    @rate.setter
    def rate(self, value):
        if value is None or value < 0:
            raise Exception('Min rate is 0.')

        self._rate = value


class BMW(Car):

    def _check(self):
        pass

    def brake(self):
        self._check()

        self.__transmit()  # THIS IS ALSO WRONG  --##--## Why?

    # THIS IS ALSO WRONG
    # def __transmit(self):   --##--## Why? For it overriden the parent's private attribute??
    #     pass

    @staticmethod
    def get_brand():
        return 'BMW'

    @staticmethod
    def do_something():
        BMW.get_brand()
        Car.get_brand()


class Z20(BMW):
    def __init__(self):
        super().__init__()
        self._model = 'Z20'


my_car = Car()
my_car.start()
my_car.run()
my_car._check()  # THIS IS WRONG, NOT ALLOWED.

my_bmw = Car()
my_bmw.start()
my_bmw.run()
my_bmw._check()  # THIS IS WRONG, NOT ALLOWED.
# my_bmw.__transmit()  THIS IS WRONG, NOT ALLOWED.


# subclass

# isinstance first input can be anything.
# issubclass first input must be a class not an object, otherwise it raises an error.

print(issubclass(BMW, Car))
print(issubclass(Car, Car))
print(isinstance(my_bmw, Car))

# print(issubclass(my_bmw, Car)) # this is wrong because my_bmw is an object not a class.

# STATIC METHOD, PROPERTIES:

# STATIC METHOD:

# THIS IS WRONG BECAUSE run is a method (instance method)
# Car.run()
my_bmw.run()  # THIS IS CORRECT

# Z20.get_brand() # WRONG IF IT IS AN INSTANCE METHOD.

my_z20 = Z20()
my_z20.get_brand()

Z20.get_brand()

# property:

print(my_z20.model)
print(my_bmw.rate)
my_bmw.rate = 10
print(my_bmw.rate)

# WRONG BECAUSE model is read only.
# my_z20.model = 'NEW'
