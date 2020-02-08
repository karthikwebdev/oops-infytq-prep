num = int(input())
for i in range(num):
    name = input()
    if(len(name)%2 == 0 and (name == name[::-1])):
        print("YES EVEN")
    elif(name == name[::-1]):
        print("YES ODD")
    else:
        print("NO")
