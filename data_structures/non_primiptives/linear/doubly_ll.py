'''
Doubly Linked Lists
'''


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None
