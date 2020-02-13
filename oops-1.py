class Parent:
    def __init__(self,num):
        self.num = num
class Child(Parent):
    def __init__(self,num):
        super().__init__(num)
        self.num = 12

c = Child(3)
print(c.num)
        
