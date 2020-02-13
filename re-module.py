import re
str = ' abc.a1bc. a23kar4thik6 abc abc'

for match in  re.compile(r'abc$').finditer(str):
    print(match)

#compile(r'.').finditer(str) returns iterables with every char 
#compile(r'\.').finditer(str) returns iterables which  . in str
#compile(r'\d').finditer(str) returns iterables which  digits in str
#compile(r'\D').finditer(str) returns iterables which  is not digits in str
#compile(r'\w').finditer(str) returns iterables which  is between (a-z,A-Z,0-9) in str
#compile(r'\W').finditer(str) returns iterables which  is NOT A WORD CHARACTER in str
#compile(r'\s').finditer(str) returns iterables which  is whitespace(space,tab,newline) in str
#compile(r'\S').finditer(str) returns iterables which  is not whitespace(space,tab,newline) in str
#compile(r'\babc').finditer(str) returns iterables which  is starting with whitespace and has abc in str
#compile(r'\Babc').finditer(str) returns iterables which  is starting with no whitespace and has abc in str
#compile(r'^abc').finditer(str) returns iterables which  is starting with abc
#compile(r'abc$').finditer(str) returns iterables which  is ending with abc

