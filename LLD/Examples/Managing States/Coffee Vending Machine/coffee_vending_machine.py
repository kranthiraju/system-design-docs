from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum
import time


# Enums
class Ingredient(Enum):
    COFFEE="COFFEE"
    MILK="MILK"
    WATER="WATER"
    SUGAR="SUGAR"

class CoffeeType(Enum):
    EXPRESSO="EXPRESSO"
    AMERICANO="AMERICANO"
    CAPPUCCINO="CAPPUCCINO"

# States
class VendingMachineState(ABC):
    def __init__(self, machine):
        self.machine: CoffeeVendingMachine = machine

    @abstractmethod
    def select_coffee(self, coffee) -> None:
        pass

    @abstractmethod
    def insert_money(self, money: int) -> None:
        pass

    @abstractmethod
    def dispense_coffee(self) -> None:
        pass

class IdleState(VendingMachineState):
    def select_coffee(self, coffee) -> None:
        self.machine._set_selected_coffee(coffee)
        self.machine._set_machine_state(SelectingState(self.machine))
        print(f"{coffee.coffee_type} selected. Price: {coffee.get_price()}.")

    def insert_money(self, money) -> None:
        print("Please select the coffee type first!!!")

    def dispense_coffee(self) -> None:
        print("Please select the coffee type first!!!")

class SelectingState(VendingMachineState):
    def select_coffee(self, coffee) -> None:
        print("Already selected the coffee type, Pay the money!!!")

    def insert_money(self, money) -> None:
        if money >= self.machine.selected_coffee.get_price():
            self.machine._set_money_inserted(money)
            self.machine._set_machine_state(PaidState(self.machine))
            print(f"Inserted {money}.")
        else:
            print(f"Please insert enough {self.machine.selected_coffee.get_price()} money first.")
            self.machine._set_machine_state(IdleState(self.machine))
            self.machine.reset()

    def dispense_coffee(self) -> None:
        print("Pay the money for coffee first!!!")

class PaidState(VendingMachineState):
    def select_coffee(self, coffee) -> None:
        print("Already selected the coffee type, wait for dispense!!!")

    def insert_money(self, money) -> None:
        print("Already paid for coffee, wait for dispense!!!")

    def dispense_coffee(self) -> None:
        inventory = self.machine.inventory
        coffee = self.machine.selected_coffee
        reciepe = coffee.get_reciepe()

        if not inventory.has_ingredient(reciepe):
            print(f"Ingredients are Out-Of-Stock, Refunding your money...")
            self.machine._set_machine_state(OutofIngredientState(self.machine))
            return

        # Prepare the coffee
        inventory.reduce_stock(reciepe)
        coffee.prepare()

        # Calculate the change
        change = self.machine.money_inserted - coffee.get_price()
        if change > 0:
            print(f"Here's your change: {change}")

        self.machine._set_machine_state(IdleState(self.machine))

class OutofIngredientState(VendingMachineState):
    def select_coffee(self, coffee) -> None:
        print("Sorry, we are sold out.")

    def insert_money(self, money) -> None:
        print("Sorry, we are sold out.")

    def dispense_coffee(self) -> None:
        print("Sorry, we are sold out.")



class Inventory:
    def __init__(self):
        self.stock: Dict[str, int] = {}

    def add_stock(self, ingredient: Ingredient, quantity: int):
        self.stock[ingredient] = self.stock.get(ingredient, 0) + quantity
        print(f"Stock added: {ingredient.value, quantity}")

    def reduce_stock(self, reciepe: Dict[Ingredient, int]):
        if self.has_ingredient(reciepe):
            for ingredient, quantity in reciepe.items():
                if ingredient in self.stock:
                    self.stock[ingredient] -= quantity

    def has_ingredient(self, reciepe: Dict[Ingredient, int]) -> bool:
        for ingredient, quantity in reciepe.items():
            if quantity > self.stock[ingredient]:
                return False

        return True

    def print_inventory(self):
        if self.stock:
            print("\n----- Ingredients -----")
            for ingredient, quantity in self.stock.items():
                print(f"{ingredient} : {quantity}")
            print("-----------------------")


# Coffee's class
class Coffee(ABC):
    def __init__(self):
        self.coffee_type = "Unknown coffee"

    def prepare(self):
        print(f"\nPreparing your {self.coffee_type}...")
        time.sleep(2)
        print(f"{self.coffee_type} is ready!")

    @abstractmethod
    def get_reciepe(self) -> Dict[Ingredient, int]:
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

class Expresso(Coffee):
    def __init__(self):
        super().__init__()
        self.coffee_type = "Expresso"

    def get_reciepe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE: 7, Ingredient.WATER: 30, Ingredient.SUGAR: 10}

    def get_price(self) -> int:
        return 150

class Cappuccino(Coffee):
    def __init__(self):
        super().__init__()
        self.coffee_type = "Cappuccino"

    def get_reciepe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE: 5, Ingredient.MILK: 40, Ingredient.WATER: 30, Ingredient.SUGAR: 15}

    def get_price(self) -> int:
        return 250

class Americano(Coffee):
    def __init__(self):
        super().__init__()
        self.coffee_type = "Americano"

    def get_reciepe(self) -> Dict[Ingredient, int]:
        return {Ingredient.COFFEE: 7, Ingredient.MILK: 50, Ingredient.WATER: 20, Ingredient.SUGAR: 20}

    def get_price(self):
        return 200


# Factory class
class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type: CoffeeType) -> Coffee:
        if coffee_type == CoffeeType.EXPRESSO:
            return Expresso()
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return Cappuccino()
        elif coffee_type == CoffeeType.AMERICANO:
            return Americano()
        else:
            raise ValueError(f"Unsupportted coffee type: {coffee_type}")

# Main Class
class CoffeeVendingMachine:
    def __init__(self):
        self.inventory: Inventory = Inventory()
        self.machine_state: VendingMachineState = IdleState(self)
        self.selected_coffee: Coffee = None
        self.money_inserted: int = None

    def add_stock(self, ingredient: Ingredient, quantity: int):
        self.inventory.add_stock(ingredient, quantity)

    def select_coffee(self, coffee_type: CoffeeType):
        coffee = CoffeeFactory.create_coffee(coffee_type)

        self.machine_state.select_coffee(coffee)

    def insert_money(self, money: int):
        self.machine_state.insert_money(money)

    def dispense_coffee(self):
        self.machine_state.dispense_coffee()

    def _set_selected_coffee(self, coffee):
        self.selected_coffee = coffee

    def _set_money_inserted(self, money: int):
        self.money_inserted = money

    def _set_machine_state(self, state):
        self.machine_state = state

    def reset(self):
        self.selected_coffee = None
        self.money_inserted = None

