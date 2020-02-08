import string
num = int(input())
for i in range(num):
    word = input()
    out = ''
    for i in word:
        if(i in string.ascii_uppercase):
            out += str( ord(i)-64 )
        elif(i in string.ascii_lowercase):
            out += str( ord(i)-96 )
        else:
            out += '$'
    print(out)
            
