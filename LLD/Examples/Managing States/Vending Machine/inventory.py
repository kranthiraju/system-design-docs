from typing import Dict
from item import Item
from collections import defaultdict

class Inventory:
    def __init__(self):
        self.items_map: Dict[str, Item] = defaultdict(Item)
        self.stock_map: Dict[str, int] = defaultdict(int)

    def add_item(self, item: Item, quantity):
        self.items_map[item.code] = item
        self.stock_map[item.code] += quantity
        print(f"{quantity} - {item.name} were added")

    def reduce_stock(self, item_code) -> None:
        self.stock_map[item_code] -= 1

    def is_available_item(self, item_code) -> bool:
        return self.stock_map[item_code] > 0

    def get_item(self, item_code):
        return self.items_map[item_code]