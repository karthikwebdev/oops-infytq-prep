class Queue:
    def __init__(self,size):
        self.list = []
        self.front = -1
        self.rear = -1
        self.size = size
    def enque(self,val):
        if(self.size-1 == self.rear):
            print("queue is full")
        elif(self.rear == -1 and self.front == -1):
            self.list.append(val)
            self.front = 0
            self.rear = 0 
        else:
            self.list.append(val)
            self.rear += 1
    def deque(self):
        if(self.rear == -1 and self.front == -1):
            print("queue is empty")
        else:
            self.list.pop(0)
            self.rear -= 1
            if(self.rear == -1):
                self.front = -1 

    def display(self):
        for i in self.list[::-1]:
            print(i)

size = int(input("enter the size of queue"))
q1 = Queue(size)
while(True):
    s = int(input("1.enque 2.deque 3.display 4.exit"))
    if(s == 1):
        val = int(input("enter value to add"))
        q1.enque(val)
    elif(s == 2):
        q1.deque()
    elif(s == 3):
        q1.display()
    else:
        break