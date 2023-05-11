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
        self.stack.append(val)

    def pop(self) -> int:
        return self.stack.pop()

    def print(self):
        print(f"{self.stack} <=")

    def contains(self, val) -> bool:
        return val in self.stack



if __name__ == "__main__":
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    s.print()
    print(s.pop())
