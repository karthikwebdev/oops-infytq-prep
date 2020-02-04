a = input()
b = input()
flag = False
if(len(a)==len(b)):
    for i in range(len(a)):
        if(a[i]<=b[i]):
            flag = True    
        else:
            flag = False
            break    
else:
    print("NO")
