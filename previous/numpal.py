num = input()
num = int(num) + int(num[::-1])
num = str(num)
while True:
    if(num == num[::-1]):
        print(num)
        break
    else:
        num = int(num) + int(num[::-1])
        num = str(num)
