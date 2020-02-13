#------------ArthmeticError-------------
# there are 3 types of arithmeticError 1.OverflowError  2.ZeroDivisionError 3.FloatingPointError 

#overflow error exists when number is out of range
#zerodivision error exists when num is divided by 0
#floating point error occurs when we make something that is not possible by floating point number


# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print("there is an exception :",z)





#next type of error was LookupError
#KeyError is used for calling key that doesnt exists
#IndexError is used for if we call out of range
# 
# 
# 
# 
#
# try:  
#     a = [1, 2, 3]  
#     print(a[3])  
# except LookupError:        ---we can also use IndexError as it is index error 
#     print("Index out of bound error.")
# else:  
#     print("Success")



#AttributeError this exists when an attribute called that doesnt exists

# class Attributes(object): 
#     pass
  
# try:
#     object = Attributes() 
#     print(object.attribute)
# except AttributeError:
#     print("No such attribute")



# if we import a module that doesnt exists then ImportError

# try:
#     import x
# except ImportError:
#     print("no such module")





#NameError for variables that are not defined





#Keyboardinterrupt for any press like ctrl + c




