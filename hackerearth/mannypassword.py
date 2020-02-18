num = int(input())
li = [input() for i in range(num)]

for i in li:
    if(i[::-1] in li):
       print(len(i),end=" ")
       print(i[int(len(i)/2)])
       break
    
