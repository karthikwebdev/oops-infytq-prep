t = int(input())
for i in range(t):
    str,n,m =input().split()
    n = int(n)
    m = int(m)
    mids = "".join(reversed(sorted(str[n:m+1])))
    print(str[0:n] + mids + str[m+1:])
    
