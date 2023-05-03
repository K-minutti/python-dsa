'''
Deep dive into linked lists
'''

# Linked lists consist of nodes
# and pointers

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node: Node=None):
        self.head = node

    def add(self, node: Node):
        if node:
            if self.head is None:
                self.head = node
            else:
                last_node = self.get_last_node()
                last_node.next = node

    def get_last_node(self) -> Node:
        if not self.head:
            raise ValueError("Empty Linked List")
        n = self.head
        while(n.next):
            n = n.next
        return n

    def pop(self) -> Node:
        """remove last node"""
        current = self.head
        assert current != None, "Cannot call pop on empty list"

        prev = current
        while (current.next):
            prev = current
            current = current.next
        
        if self.head.data == current.data:
            self.head = None
        else:
            prev.next = None
        return current

    def print(self) -> None:
        current = self.head
        values = []
        while(current):
            values.append(f"[{current.data}]->")
            current = current.next
        print("".join(values))


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(Node(7))
    ll.add(Node(5))
    ll.add(Node(10))
    ll.add(Node(11))
    ll.print()
    n = ll.pop()
    ll.print()
    assert n.data == 11
