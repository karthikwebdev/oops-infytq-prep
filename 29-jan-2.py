#multiple inheritance 
class car:
    def __init__(self,name):
        print(name)
class bmw(car):
    def __init__(self,name,model):
        super().__init__(name)
        print("bmw model:",model)
class maruthi(car):
    def __init__(self,name,model):
        super().__init__(name)
        print("maruthi model:",model)
c = bmw("car","x20")
x = maruthi(" car"," u5000")