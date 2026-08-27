from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head: Node = Node(None, None)
        self.tail: Node = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node):
        """
        add the node at head
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        """
        remove the selected node
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_first(self, node: Node):
        """
        move the selected node to first
        """
        self.remove_node(node)
        self.add_first(node)

    def remove_last_node(self):
        """
        remove the last node
        """
        if self.tail.prev == self.head:
            return None
        last_node = self.tail.prev
        self.remove_node(last_node)

        return last_node
        