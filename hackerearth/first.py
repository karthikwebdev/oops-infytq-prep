num = int(input())

for i in range(num):
    str = ''
    inp = input()
    for i in inp:
        if(i in str):
            pass
        else:
            str += i
    print(str)
