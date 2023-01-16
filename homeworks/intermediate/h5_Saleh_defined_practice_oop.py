# class Vehicle:
#
#     vehicle_color = 'white'
#
#     def __init__(self, name, max_speed, mileage, capacity):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def seating_capacity(self):
#         return f"The seating capacity of a {self.name} is {self.capacity} passengers"
#
#     def fare(self):
#         return self.capacity * 100
#
#     def __str__(self):
#         return f'Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}' \
#                f' with color: {Vehicle.vehicle_color}'
#
#
# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, capacity):
#         super().__init__(name, max_speed, mileage, capacity)
#         # also: super(Car, self).__init__(name, max_speed, mileage)
#
#     def fare(self):
#         return self.capacity * 110
#
#
# bus1 = Bus('Volvo', 140, 1000,50)
# print(bus1)
# print(bus1.seating_capacity())
# print(bus1.fare())
# print(bus1.vehicle_color)
# print(Bus.vehicle_color)
# print(Vehicle.vehicle_color)


class Rectangular:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

    def display(self):
        print(f'w: {self.width}, l: {self.length}, p: {self.perimeter()}, a: {self.area()}')


class Parallelepiped(Rectangular):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    def perimeter(self):
        return 13

    def area(self):
        return 14

    def display(self):
        pass

    def volume(self):
        return self.width * self.length * self.height


p1 = Parallelepiped(1, 2, 1)
print(p1.volume())

