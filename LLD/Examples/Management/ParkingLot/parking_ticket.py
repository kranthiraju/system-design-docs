import time
import uuid
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingTicket:
    def __init__(self, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.spot: ParkingSpot = spot
        self.vehicle: Vehicle = spot.park_vehicle
        self.entry_timestamp = int(time.time() * 1000)
        self.exit_timestamp = 0

    def set_exit_timestamp(self):
        self.exit_timestamp = int(time.time() * 1000)