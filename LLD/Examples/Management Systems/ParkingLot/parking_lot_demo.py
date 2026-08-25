import time
from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from vehicle import Bike, Car, Truck

class ParkingLotDemo:
    @staticmethod
    def main():
        parking_lot: ParkingLot = ParkingLot.get_instance()

        # add floors with spots
        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot("F1-01", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F1-02", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F1-03", VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot("F1-04", VehicleSize.SMALL))

        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot("F2-21", VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot("F2-22", VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot("F2-23", VehicleSize.MEDIUM))
        floor2.add_spot(ParkingSpot("F2-24", VehicleSize.LARGE))
        floor2.add_spot(ParkingSpot("F2-25", VehicleSize.LARGE))

        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)

        # add vehicles
        print("---- Vehicles Entries ----")

        bike1 = Bike("B1-2309")
        car1 = Car("C3-3837K")
        truck1 = Truck("T32-OP309")

        bike1_ticket = parking_lot.park_vehicle(bike1)
        car1_ticket = parking_lot.park_vehicle(car1)
        truck1_ticket = parking_lot.park_vehicle(truck1)

        parking_lot.display_availability()

        # unpark vehicle
        time.sleep(5)
        parking_lot.unpark_vehicle(truck1_ticket)

        # add more vehicles
        car2 = Car("C42-3837K")
        car3 = Car("C3-42D37KP")
        car4 = Car("C30-3837KK")

        parking_lot.park_vehicle(car2)
        parking_lot.park_vehicle(car3)
        parking_lot.park_vehicle(car4)

        parking_lot.display_availability()



if __name__ == "__main__":
    ParkingLotDemo.main()