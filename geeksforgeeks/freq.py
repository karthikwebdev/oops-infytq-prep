#code
num = int(input())
for i in range(num):
    str = [i for i in input()]
    new = []
    for i in str:
        if(i not in new):
            new.append(i)
    print(''.join(new))
