t = int(input())
for i in range(t):
    num = input()
    if(num == num[::-1]):
        print("YES")
    else:
        print("NO")
