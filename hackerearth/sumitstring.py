num = int(input())
for i in range(num):
    str = input()
    for i in range(len(str)-1):
        if((abs(ord(str[i])-ord(str[i+1])) == 1) or (str[i]=='a' and str[i+1]=='z') or (str[i]=='z' and str[i+1]=='a') ):
            pass
        else:
            print("NO")
            break
    else:
        print('YES')
            
