n = int(input())
s = input().replace(" ","")
k= max(map(len,s.split('1')))
print(k)
l= max(map(len,s.split('0')))
print(l)
print(max(k,l))