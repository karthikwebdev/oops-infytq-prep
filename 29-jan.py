class student:
    def __init__(self,name,roll,pro,ram,hd,mram,ms,mbrand):
        self.name = name
        self.roll = roll
        self.lap = self.laptop(pro,ram,hd)
        self.lap.mob = self.lap.mobile(mram,ms,mbrand)
    def disp(self):
        print(self.name,self.roll)
        self.lap.disp()
        self.lap.mob.disp()

    class laptop:
        def __init__(self,pro,ram,hd):
            self.pro = pro
            self.ram = ram
            self.hd = hd
        def disp(self):
            print(self.pro,self.ram,self.hd)

        class mobile:
            def __init__(self,mram,ms,mbrand):
                self.mram = mram
                self.ms = ms
                self.mbrand = mbrand
            def disp(self):
                print(self.mram,self.ms,self.mbrand)
            
s1 = student("karthik","i7","i5","8gb","2tb","4gb","32gb","mi")
s1.disp()
