num = int(input())
for _ in range(num):
    n = int(input())
    li = list(map(int,input().split()))
    for i in li:
        if(li.count(i)>n/2):
            print(i)
            break
    else:
        print(-1)
