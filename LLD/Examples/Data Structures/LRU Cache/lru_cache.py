from doubly_linked_list import DoublyLinkedList
from node import Node
from typing import Dict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.doubly_linked_list = DoublyLinkedList()
        self.cache: Dict[str, Node] = {}

    def get(self, key) -> str:
        """
        1. get the value of key from cache/map
        2. Update the order from doubly linkedlist as latest recently used
        """
        if key not in self.cache:
            return None
        # Update the order from doubly linkedlist as latest recently used
        node = self.cache[key]
        self.doubly_linked_list.move_to_first(node)
        return node.value

    def put(self, key, value):
        """
        1. create a new node if key is not there
        2. then update in linkedlist
        """
        if key in self.cache:
            existing_node = self.cache[key]
            existing_node.value = value
            self.doubly_linked_list.move_to_first(existing_node)
        else:
            if len(self.cache) >= self.capacity:
                # excess then remove least used
                lru_node = self.doubly_linked_list.remove_last_node()
                if lru_node:
                    del self.cache[lru_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.doubly_linked_list.add_first(new_node)