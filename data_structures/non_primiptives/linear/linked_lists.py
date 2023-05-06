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
        self.size = 0

    def add(self, node: Node):
        if node:
            if self.head is None:
                self.head = node
            else:
                last_node = self.get_last_node()
                last_node.next = node
            self.size += 1

    def add_front(self, node: Node):
        if node:
            if self.head is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
            self.size +=1

    def get_last_node(self) -> Node:
        if not self.head:
            raise ValueError("Empty Linked List")
        n = self.head
        while(n.next):
            n = n.next
        return n
    
    def remove(self, data) -> bool:
        """remove node by value"""
        current = self.head
        assert current != None, "Cannot call remove() on empty list" 
        while (current.next):
            if current.next.data == data:
                next_obj = current.next.next
                current.next = next_obj
                self.size -= 1
                return True
            current = current.next
        return False

    def pop(self) -> Node:
        """remove last node"""
        current = self.head
        assert current != None, "Cannot call pop() on empty list"

        prev = current
        while (current.next):
            prev = current
            current = current.next
        
        if self.head.data == current.data:
            self.head = None
        else:
            prev.next = None
        self.size -= 1
        return current
    
    
    def unshift(self) -> Node:
        """remove first node"""
        current = self.head
        assert current != None, "Cannot call unshift() on empty list"

        self.head = current.next
        self.size -= 1
        return current

    def print(self) -> None:
        current = self.head
        values = []
        while(current):
            values.append(f"[{current.data}]->")
            current = current.next
        print("".join(values))

    def find(self, val) -> bool:
        current = self.head
        if current is None:
            return False
        while(current):
            if val == current.data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(Node(7))
    ll.add(Node(5))
    ll.add(Node(10))
    ll.add(Node(11))
    ll.print()
    n = ll.pop()
    ll.print()
    b = ll.unshift()
    ll.print()
    print(f"list size: {ll.size}")
    ll.add_front(Node(3))
    ll.print()
    print(f"list size: {ll.size}")
    print(f"8 in list: {ll.find(8)}")
    ll.remove(5)
    ll.print()
    ll.remove(10)
    ll.print()
    assert n.data == 11
