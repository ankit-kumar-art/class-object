from collections import deque
class stackUsingqueue:
    def __init__(self):
        self.queue=deque()
    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        if len(self.queue)==0:
            return "stack is empty"
        x=self.queue.popleft()
        return x
    def peek(self):
        if len(self.queue)==0:
            return "stack is empty"
        return self.queue[0]
    
item=stackUsingqueue()
item.push(10)
item.push(49)
print(item.pop())
print(item.peek())
print(item.pop())
print(item.pop())
    
        