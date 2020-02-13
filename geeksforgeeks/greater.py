num = int(input())
for _ in range(num):
    n = int(input())
    li = list(map(int,input().split()))
    lis = []
    for i in range(len(li)-1):
        for j in li[i+1:]:
            if(j>li[i]):
                lis.append(j)
                break
        else:
            lis.append(-1)
    lis.append(-1)
    for i in lis:
        print(i,end = ' ')
    print()
