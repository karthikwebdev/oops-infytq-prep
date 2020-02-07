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

    def delHead(self):
        if self.head == None:
            print("Empty list")
        else:
            self.temp = self.head
            self.head = self.head.add
            self.temp.add = None
            del self.temp

    def display(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data)
            self.temp = self.temp.add

    def insertAtPosition(self,val,pos):
        self.temp = self.head
        if  not self.head:
            self.insert(val)
        else:
            while pos-2:
                if( not self.temp.add):
                    break
                self.temp = self.temp.add
                pos-=1
            nn = Node(val)
            nn.add = self.temp.add
            self.temp.add = nn

    def deleteAtPosition(self,pos):
        self.temp = self.head
        if(not self.temp):
            print("Empty List")
        elif(pos == 1):
            self.delHead()
        else:
            while pos-2:
                if self.temp.add == None:
                    print("List is not sufficient")
                    break
                self.temp = self.temp.add
                pos -= 1
            else:
                self.temp1 = self.temp.add
                self.temp.add = self.temp.add.add
                del self.temp1

l1 = Linkedlist()

while True:
    ch = int(input("1.insert  2.delete 3.display 4.delete head 5.insert in position 6.delete in a position"))
    if(ch == 1):
        val = int(input("enter value to insert"))
        l1.insert(val)
    elif(ch == 2):
        l1.delete()
    elif(ch == 3):
        l1.display()
    elif(ch == 4):
        l1.delHead()
    elif(ch == 5):
        val = int(input("insert value"))
        pos = int(input("enter position"))
        l1.insertAtPosition(val,pos)
    elif(ch == 6):
        pos = int(input("enter position to delete"))
        l1.deleteAtPosition(pos)
    else:
        break