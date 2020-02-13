string = "{[()]}[[]"
lst1 =['{', '(', '['] 
lst2 =['}', ')', ']'] 
lst =[] 
Dict ={ ')':'(', '}':'{', ']':'['} 
a = b = c = 0
if string[0] in lst2: 
	print(1) 	
else:
	for i in range(0, len(string)): 
		if string[i] in lst1: 
			lst.append(string[i]) 
		else: 	 
			if len(lst)== 0 and (string[i] in lst2): 
				print(i + 1) 
				break
			else:	 
				if Dict[string[i]]== lst[len(lst)-1]: 
					lst.pop() 
				else: 	 
					print(i + 1) 
					break		 
	if len(lst)== 0 and c == 0: 
		print(0)  
