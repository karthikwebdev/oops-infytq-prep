num = int(input())
for i in range(num):
    print(".".join(list(input().split('.'))[::-1]))
