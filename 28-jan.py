class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def disp(self):
        print(self.name,self.roll)
    class laptop:
        def __init__(self,pro,ram,hd):
            self.pro = pro
            self.ram = ram
            self.hd = hd
        def disp(self):
            print(self.pro,self.ram,self.hd)

s1 = student("karthik","i7")
s1.disp()
l1 = s1.laptop("i5","8gb","2tb")
l1.disp()