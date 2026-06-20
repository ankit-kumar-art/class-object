class Queue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def enqueue(self,item):
        self.item.append(item)
    def dequeue(self):
        if len(self.item)==0:
            print("dequue from empty list not do")
            return
        x=self.item.pop(0)
        return x
    def front(self):
        if len(self.item)==0:
            print("cannot  peek ,queue is empty")
        return self.item[0]
    def rear(self):
        if len(self.item)==0:
            return "cannot read,queue is empty"
        return self.item[-1]
    def size(self):
        return len(self.item)
queue=Queue()
print(queue.is_empty() )         
queue.enqueue(45)
queue.enqueue(34)
print(f"front eleemnt is :={queue.front()}")
print(f"rear eleemnt is :={queue.rear()}")
queue.rear()

    
                