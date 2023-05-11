'''
In python a stack can be easily implemented with a list
Operations
add
pop


'''



class Stack:
 
    def __init__(self):
        self.stack = []

    def add(self, val: int):
        self.append(val)

    def pop(self) -> int:
        return self.pop()

    def contains(self, val) -> bool:
        return val in self.stack




