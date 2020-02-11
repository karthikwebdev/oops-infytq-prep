str = input()
out =[]
l = [i for i in str if i.isdigit()]
for i in l:
    if(i not in out):
        out.append(i)
out = list(dict.fromkeys(out))
out.sort()
for i in out:
    if(int(i) % 2 == 0):
        ev = i
        out.remove(i)
        out.reverse()
        out.append(ev)
        out = "".join(out)
        print(int(out))
        break
else:
    print(-1)
    


        
