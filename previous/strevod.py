str = input().split(',')
ans = []
for i in str:
    x = 0
    num = i.split(':')[1]
    for j in num:
        x = x + int(j)*int(j)
    if(x%2==0):
        ans.append(i.split(':')[0][-2:]+i.split(':')[0][:-2])
    else:
        ans.append(i.split(':')[0][1:]+i.split(':')[0][0])
print(ans)
