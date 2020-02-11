def firsteven(list):
    for i in list:
        if int(i) % 2 == 0:
            return i
    else:
        return firstodd(list)

def firstodd(list):
    for i in list:
        if int(i) % 2 != 0:
            return i
    else:
        return firsteven(list)

str = input()
count = 0
li = []
out = ''
c = 0
for i in str:
    if not i.isalnum():
        count += 1
    if i.isdigit():
        li.append(i)
if(count%2 == 0):
    while li:
        if(c%2==0):
            out += firsteven(li)
            li.remove(firsteven(li))
            c += 1
        else:
            out += firstodd(li)
            li.remove(firstodd(li))
            c += 1
else:
    while li:
        if(c%2!=0):
            out += firsteven(li)
            li.remove(firsteven(li))
            c += 1
        else:
            out += firstodd(li)
            li.remove(firstodd(li))
            c += 1
print(int(out))    
        
    
        
