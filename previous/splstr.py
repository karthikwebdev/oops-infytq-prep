#reverse a string keeping the special characters at same place

#input ------> #ab$is
#output -----> #si$ba


import string as mod
str = input()
revno = ''
out = ''
for i in str:
    if((i in mod.ascii_lowercase) or (i in mod.ascii_uppercase)):
        revno += i
revno = revno[::-1]
for i in range(len(str)):
    if((str[i] in mod.ascii_lowercase) or (str[i] in mod.ascii_uppercase)):
        out += revno[0]
        revno = revno[1:]
    else:
        out += str[i]
print(out)
