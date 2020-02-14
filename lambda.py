#lambdas or anonymous  functions

from functools import reduce

# f = lambda a: a*a

# print(f(2))

y = lambda x: (x%2)==0
print(y(4))

#filter takes two arguements a function and iterable and filters if function returns true


li = [2,3,4,5,6,1,7,2]
print(list(filter(lambda n:n%2==0,li)))

#map takes 2 arguements a function and iterable and applies  it to every member of iterable


print(list(map(lambda x:x+2,li)))

#reduce is for using all and producing one value

print(reduce(lambda a,b:a+b,li))

