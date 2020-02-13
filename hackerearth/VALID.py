t = int(input())
for _ in range(t):
    num = input()
    if(num.isnumeric() and num[0] != 0 and len(num) == 10):
        print("YES")
    else:
        print("NO")
