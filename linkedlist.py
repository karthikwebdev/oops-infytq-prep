class Node:
    def __init__(self,val):
        self.data = val 
        self.add = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.last = None
    def insert(self,val):
        nn = Node(val)
        if(self.head==None):
            self.head = nn
            self.last = nn
        else:
            self.last.add = nn
            self.last = nn    
    def delete(self):
        self.temp = self.head
        if(self.temp == None):
            print("empty linkedlist")
        elif(self.head == self.last):
            del self.head
            self.head = None
            self.last = None
        else:
            while self.temp.add.add:
                self.temp = self.temp.add
            self.temp.add = None
            del self.last
            self.last = self.temp
    def display(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data)
            self.temp = self.temp.add

l1 = Linkedlist()
while True:
    ch = int(input("1.insert  2.delete 3.display 4.exit"))
    if(ch == 1):
        val = int(input("enter value to insert"))
        l1.insert(val)
    elif(ch == 2):
        l1.delete()
    elif(ch == 3):
        l1.display()
    else:
        break

