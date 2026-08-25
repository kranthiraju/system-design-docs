from abc import ABC, abstractmethod
from item import Item
from coin import Coin

class VendingState(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def select_item(self, item) -> None:
         pass

    @abstractmethod
    def insert_coin(self, coin: Coin) -> None:
        pass

    @abstractmethod
    def dispense(self) -> None:
        pass

    @abstractmethod
    def refund(self) -> None:
        pass


class IdleState(VendingState):
    def select_item(self, item) -> None:
        if not self.machine.inventory.is_available_item(item):
            print(f"Item not available !")
            return

        self.machine.set_selected_item(item)
        self.machine.inventory.reduce_stock(item)
        self.machine.set_state(ItemSelectedState(self.machine))

    def insert_coin(self, coin: Coin) -> None:
        print("Please select an Item before inserting money.")

    def dispense(self):
        print("No item selected.")

    def refund(self):
        print("No money to refund.")




class ItemSelectedState(VendingState):
    def select_item(self, item: Item) -> None:
        print("Item already selected. Please insert money.")

    def insert_coin(self, coin: Coin) -> None:
        self.machine.add_balance(coin.get_value())
        print(f"Coin inserted: ${coin.get_value()}")

        selected_item = self.machine.get_selected_item()
        if selected_item and self.machine.balance >= selected_item.price:
            print("Sufficient money received.")

            self.machine.set_state(HasMoneyState(self.machine))

    def dispense(self):
        print("Please insert the money for selected item.")

    def refund(self):
        print("No money to refund.")




class HasMoneyState(VendingState):
    def select_item(self, item: Item) -> None:
        print("Item already selected. Please dispense.")

    def insert_coin(self, coin: Coin) -> None:
        self.machine.add_balance(coin.get_value())
        print(f"Additional coin inserted: ${coin.get_value()} - will be returned as change.")

    def dispense(self):
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense_item()

    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()

        self.machine.set_state(IdleState(self.machine))


class DispensingState(VendingState):
    def select_item(self, item: Item) -> None:
        print("Currently dispensing. Please wait...")

    def insert_coin(self, coin: Coin) -> None:
        print("Currently dispensing. Please wait...")

    def dispense(self):
        print("Currently dispensing. Please wait...")

    def refund(self):
        print("Currently dispensing. Please wait...")