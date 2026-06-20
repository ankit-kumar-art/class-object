#==========================level order==================
from collections import deque
def leveoreder(node):
    result=[]
    queue=deque([])
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)   
    return result  

#=========================tree=============
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks=Node("drinks")  
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanta

drinks.left=hot
drinks.right=cold
        
        

print(leveoreder(drinks))    