class stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if len(self.item)==0:
            return "stack is empty"
        x=self.item.pop()
        return x
    def top(self):
        if len(self.item)==0:
            return "cannot top,stack is empty"
        return self.item[-1]
    def size(self):
        return len(self.item)   
Stack=stack() 
Stack.push(3)
Stack.push(4)        
Stack.push(4)
print(Stack.top())    
print(f"stack content={Stack}")
print(f"pop element ={Stack.pop()}")
print(f"pop element ={Stack.pop()}")
print(f"pop element ={Stack.pop()}")
print(Stack.top())    
                    
