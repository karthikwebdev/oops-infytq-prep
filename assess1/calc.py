def c(x,y):
    while(x!=y):
        if(x>y):
            return c(x-y,y)
        else:
            return c(x,y-x)
    return x
print(c(10,55),c(60,30),c(27,47),c(45,30))


