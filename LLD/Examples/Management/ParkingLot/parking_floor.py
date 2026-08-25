from typing import List, Dict
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots : Dict[str, ParkingSpot] = {}

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots[spot.spot_id] = spot

    def find_available_spot(self, vehicle: Vehicle):
        available_spots = [
            spot
            for spot in self.spots.values()
            if not spot.is_occupied and spot.can_fit_vehicle(vehicle)
        ]

        if available_spots:
            return available_spots[0]

        return None


