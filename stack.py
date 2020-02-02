#operations of stack
# push pop 
# top = none
# size = n

class Stack:
    def __init__(self,size):
        self.top,self.size,self.list = -1,size,[]
    def push(self,val):
        if(self.top < size-1):
            self.list.append(val)
            self.top = self.top + 1
        else:
            print("stack overflow")            
    def pop(self):
        if(self.top >= 0):
            self.list.pop()
            self.top = self.top - 1
        else:
            print("stack underflow")
    def show(self):
        for i in self.list[::-1]:
            print(i)

size = int(input("enter size of stack"))
s = Stack(size)
while True:
    ch = int(input("1.push 2.pop 3.display 4.exit"))
    if(ch == 1):
        val = int(input("enter value to push"))
        s.push(val)
    elif(ch == 2):
        s.pop()
    elif(ch == 3):
        s.show()
    else:
        break
