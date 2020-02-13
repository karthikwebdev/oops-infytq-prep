num = int(input())
for i in range(num):
    n = int(input())
    li = list(map(int,input().split()))
    act = sum(list(range(1,n+1)))
    li = sum(li)
    print(act-li)
    
