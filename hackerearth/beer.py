x = input()
y = x
n = int(input())
strli = [input() for _ in range(n)]
count = 0
newstr = ''
for i in strli:
    if(i not in x):
        print(i)
        count += 1
print(count)
        
            
