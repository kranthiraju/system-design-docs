from inventory import Inventory
from vending_state import IdleState
from vending_state import VendingState
from item import Item
from coin import Coin

class VendingMachineSystem:
    _instance = None

    def __init__(self):
        self.inventory: Inventory = Inventory()
        self.current_state = IdleState(self)
        self.selected_item = None
        self.balance = 0

    def getInstance(self):
        if VendingMachineSystem._istance is None:
            VendingMachineSystem._instance = VendingMachineSystem()

        return VendingMachineSystem._instance

    def select_item(self, item_code) -> None:
        item = self.inventory.get_item(item_code)
        print(f"Selected {item.name}. Price: ${item.price}")
        self.current_state.select_item(item_code)

    def insert_coin(self, coin: Coin) -> None:
        self.current_state.insert_coin(coin)

    def dispense(self) -> None:
        self.current_state.dispense()

    def get_selected_item(self) -> Item:
        return self.inventory.get_item(self.selected_item)

    def set_selected_item(self, item_code) -> None:
        self.selected_item = item_code

    def set_state(self, new_state: VendingState) -> None:
        self.current_state = new_state

    def add_item(self, code, name, price, quantity) -> None:
        item = Item(code,name, price)
        self.inventory.add_item(item, quantity)

    def add_balance(self, value) -> None:
        self.balance += value

    def refund_balance(self) -> None:
        print(f"Refunding balance: {self.balance}")
        self.balance = 0

    def reset(self) -> None:
        self.selected_item = None
        self.balance = 0

    def dispense_item(self) -> None:
        item = self.inventory.get_item(self.selected_item)
        if self.balance >= item.price:
            self.inventory.reduce_stock(self.selected_item)
            self.balance -= item.price
            print(f"Dispensed: {item.name}")

            if self.balance > 0:
                print(f"Returning change: {self.balance}")

            self.reset()
            self.set_state(IdleState(self))
