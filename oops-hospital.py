class hospital:
    fee = 500
    def __init__(self,name,time):
        self.name = name
        self.time = time
    def checkup(self):
        print("pay fee of",self.fee,"for",self.name,"at",self.time)
    @classmethod
    def feeinc(cls):
        cls.fee = cls.fee + 500
    
hosp1 = hospital("apollo" , "12-30")
hosp1.checkup()
hospital.feeinc()
hosp2 = hospital("kims","1-00")
hosp2.checkup()
hosp1.checkup()
        