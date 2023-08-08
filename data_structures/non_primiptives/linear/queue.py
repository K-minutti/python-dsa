'''
Queue
'''

class Queue: 

    def __init__(self):
        self.queue = []
    
    def push(self, val: int):
        self.queue.append(val)
    
    def pop(self) -> int:
        assert len(self.queue) > 0, "Cannot call pop() on empty queue"
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val
    


if __name__ == "__main__":
    s = Queue()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
