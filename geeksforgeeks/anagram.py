num = int(input())
for i in range(0,num):
    li = list(input().split())
    str1 = [i for i in li[0]]
    str2 = [i for i in li[1]]
    for i in str1:
        if(i in str2):
            str2.remove(i)
        else:
            print("NO")
            break
    else:
        if(len(str2)==0):
            print("YES")
        
