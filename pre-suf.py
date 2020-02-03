#take a string as input and print prefix and suffix that are equal
#sample inputs -> outputs  
#asa -> a ,adda -> a , safsa -> sa , asdf -> -1 
 
str = input()
answer = -1
if(str[0]==str[-1]):
    answer = str[0]
for i in range(1,len(str)//2):
    prefix = str[:i+1]
    suffix = str[len(str)-i-1:]
    print(prefix,suffix)
    if(prefix == suffix):
        answer = prefix
print(answer)