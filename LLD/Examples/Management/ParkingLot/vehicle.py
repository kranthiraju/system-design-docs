from abc import ABC
from vehicle_size import VehicleSize

class Vehicle(ABC):
    def __init__(self, number, size: VehicleSize):
        self.number = number
        self.size = size

    def get_size(self) -> VehicleSize:
        return self.size

class Bike(Vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleSize.SMALL)


class Car(Vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleSize.MEDIUM)

class Truck(Vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleSize.LARGE)