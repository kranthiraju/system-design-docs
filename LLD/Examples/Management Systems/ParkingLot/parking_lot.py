import threading
from typing import List, Dict, Optional
from collections import defaultdict
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from vehicle import Vehicle
from vehicle_size import VehicleSize
from price_strategy import FlatRatePriceStrategy

class ParkingLot:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.price_strategy = FlatRatePriceStrategy()
        self._main_lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_floor(self, floor: ParkingFloor) -> None:
        self.floors.append(floor)

    def park_vehicle(self, vehicle:Vehicle) -> Optional[ParkingTicket]:
        with self._main_lock:
            spot = None
            for floor in self.floors:
                spot = floor.find_available_spot(vehicle)
                if spot is not None:
                    break

            if spot is not None:
                spot.park_vehicle(vehicle)
                ticket = ParkingTicket(spot)
                self.active_tickets[ticket.ticket_id] = ticket

                print(f"\n Vehicle {vehicle.number} parked at spot {ticket.spot.spot_id}")
                return ticket

            print("No Available spots !!! \n")
            return None

    def unpark_vehicle(self, ticket:ParkingTicket):
        with self._main_lock:
            ticket = self.active_tickets.pop(ticket.ticket_id, None)
            if ticket is None:
                print(f"Ticket is not found for vehicle: {ticket.spot.vehicle.number}")
                return None
            
            spot = ticket.spot
            vehicle_number = spot.parked_vehicle.number
            spot.unpark_vehicle()
            ticket.set_exit_timestamp()

            
            price = self.price_strategy.calculate_price(ticket)
            print(f"Vehicle {vehicle_number} unparked from spot {ticket.spot.spot_id}. Price: ${price:.2f}")
            return None

    def display_availability(self) -> None:
        available_counts = defaultdict(int)
        for floor in self.floors:
            for spot in floor.spots.values():
                if spot.is_available():
                    available_counts[spot.spot_size.value] += 1

        print("-"*20)
        print(f"Available Spots")
        print("-"*20)

        print(f"Small : {available_counts[VehicleSize.SMALL.value]}")
        print(f"Medium : {available_counts[VehicleSize.MEDIUM.value]}")
        print(f"Large : {available_counts[VehicleSize.LARGE.value]}")
        print("-"*20)
