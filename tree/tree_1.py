# dfs(implementation preorder)
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

        
#=======================preorder==============
def preorder(node):
    if node==None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
preorder(drinks)   

#======================inorder====================
def preorder(node):
    if node==None:
        return
    preorder(node.left)
    print(node.val)
    preorder(node.right)
preorder(drinks)   

#=======================postorder====================
def preorder(node):
    if node==None:
        return
    preorder(node.left)
    preorder(node.right)
    print(node.val)
preorder(drinks)
        
        
        
    
    