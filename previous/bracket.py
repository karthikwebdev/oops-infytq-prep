while 1:   
    str = input()
    li = []
    for i in range(len(str)):
        if str[i] =='[' or str[i] == '{' or str[i] == '(':
            li.append(str[i])
        else:
            if(str[i] == ']' and len(li) and li[-1] == '['):
                li.pop()
            elif(str[i] == '}' and len(li) and li[-1] == '{' ):
                li.pop()
            elif(str[i] == ')' and len(li) and li[-1] == '('):
                li.pop()
            else:
                print(i)
                break
            
        
        
