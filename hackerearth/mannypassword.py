num = int(input())
li = []
for i in range(num):
    li.append(input())
for i in li:
    if(i[::-1] in li):
       print(len(i),end=" ")
       print(i[int(len(i)/2)])
       break
    
