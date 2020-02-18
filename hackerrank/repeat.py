s = input()
li = list(dict.fromkeys([i for i in s]))
ls = [s.count(i) for i in li]
main1 = []
main2 = []
sem1 = []
sem2 = []
for i in range(3):
    p = ls.index(max(ls))
    if(ls.count(max(ls))==1):
        main1.append(li.pop(p))
        main2.append(ls.pop(p))
    else:
        pass
print(main1,main2)
            
        
        
