num = int(input())
for i in range(num):
    newstr = ''
    rna = int(input())
    str = input()
    for i in str:
        if(i == 'A'):
            newstr += 'T'
        elif(i == 'T'):
            newstr += 'A'
        elif(i == 'G'):
            newstr += 'C'
        elif(i == 'C'):
            newstr += 'G'
        else:
            print("Error RNA nucleobases found!")
            break
    else:
        print(newstr)
            
        
        
