#code
num = int(input())
for _ in range(num):
    str1 = input()
    str2 = input()
    if((str1 == str2[-2:]+str2[:-2]) or (str1 == str2[2:]+str2[:2])):
        print(1)
    else:
        print(0)
