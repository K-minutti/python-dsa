'''
Deep dive into linked lists
'''

# Linked lists consist of nodes
# and pointers

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.head = False

class LinkedList:
    def __init__(self, node: Node):
        self.head = node

    def print(self) -> None:
        current = self.head
        values = []
        while(current):
            values.append(f"[{current.data}]->")
        print("".join(values))

