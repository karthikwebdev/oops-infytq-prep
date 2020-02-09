#program to reverse a string after removing duplicates

#input --------> google
#output --------> elog

print("".join(list(dict.fromkeys(input()))[::-1]))

