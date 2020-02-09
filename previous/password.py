def near(length,number):
    max = -1
    while(number):
        r = number%10
        number = number//10
        if(r<=length and r>max):
            max = r
    return max

        
str = input()
newstr = ''
li = list(str.split(","))
for i in li:
    l = len(list(i.split(":"))[0])
    num = int(list(i.split(":"))[1])
    val = near(l,num)
    if(val == -1):
        newstr +=  'X'
    else:
        newstr += list(i.split(":"))[0][val-1]
        

