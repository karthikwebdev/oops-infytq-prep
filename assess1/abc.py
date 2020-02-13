s = 'all3 that4 glitters8 is2 not3 gold4'
l = []
for char in s:
    if(char.isdigit()):
        l.append(int(char))
        s=s.replace(char,' ')
print(l,s)
