class student:
    cg = "Aditya Group of Institutions"  #class variables
    def __init__(self,r,n,p):#instance mutator method
        self.rollno = r     #instance variables
        self.name = n       #instance variables
        self.phno = p       #instance variables
    def display(self):      #instance accesser method
        print(self.rollno,self.name,self.phno,self.cg)
    @classmethod
    def set(cls):
        cls.cg = "aditya"
std1 = student("123","karthik",9493454298)
std1.display()
student.set()
std2 = student("121","potti",8328204888)
std2.display()
