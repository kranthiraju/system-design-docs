from coffee_vending_machine import CoffeeVendingMachine, Ingredient, CoffeeType

machine = CoffeeVendingMachine()

# initial setup: Fill inventory
machine.add_stock(Ingredient.COFFEE, 20)
machine.add_stock(Ingredient.MILK, 100)
machine.add_stock(Ingredient.WATER, 100)
machine.add_stock(Ingredient.SUGAR, 40)
machine.inventory.print_inventory()

print(f"\n{'-' * 90}")

# 1: Succeessful purchase of Expresso
print("\n --- Buy an Expresso ---")
machine.select_coffee(CoffeeType.EXPRESSO)
machine.insert_money(350)
machine.dispense_coffee()
machine.inventory.print_inventory()

print(f"\n{'-' * 90}")
# 2: buy with insufficient funds
print("\n --- Buy Cappuccino (Insufficient funds) ---")
machine.select_coffee(CoffeeType.CAPPUCCINO)
machine.insert_money(21)
machine.dispense_coffee()
machine.inventory.print_inventory()