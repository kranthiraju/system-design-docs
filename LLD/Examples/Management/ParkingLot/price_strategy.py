from abc import ABC, abstractmethod
from parking_ticket import ParkingTicket

class PriceStrategy(ABC):
    @abstractmethod
    def calculate_price(self, ticket: ParkingTicket) -> float:
        pass

class FlatRatePriceStrategy(PriceStrategy):
    RATE_PER_HOUR = 45
    def calculate_price(self, ticket: ParkingTicket) -> float:
        duration = ticket.exit_timestamp - ticket.entry_timestamp
        hours = (duration // (1000)) + 1
        return hours * self.RATE_PER_HOUR