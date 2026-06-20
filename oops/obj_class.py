class student:
    # Attributes
    #methods
    def __init__(self,name: str,age: int):
        print("this construtor")
        self.name=name
        self.age=age
        
    def display(self):
        print(self.name,self.age)    
        
        
student1=student("ankit",44)
student1.display()
        
        