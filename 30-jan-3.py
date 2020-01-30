# import keyword
# print(keyword.iskeyword("for")) - True


# print("hello","world",sep="-",end=" ")  
# print("hello","world",sep="-",end=" ")
#o/p - hello-world hello-world


# str = "I love geeksforgeeks"
# # Printing the center aligned   
# # string with fillchr  
# print ("Center aligned string with fillchr: ")  
# print (str.center(40, '#'))  
# # Printing the left aligned   
# # string with "-" padding   
# print ("The left aligned string is : ")  
# print (str.ljust(40, '-'))  
# # Printing the right aligned string  
# # with "-" padding   
# print ("The right aligned string is : ")  
# # print (str.rjust(40, '-')) 
# l = "string".center(40, '-')
# print(l)


#string formatting by different methods using % , {} , template strings

# #% formatting is similar to printf in c
# # %d - int , %f - float , %s - string , %x - hexadecimal , %o - octal , %r - raw data
# var = '15'
# print("%s"%(var)) #- 15
# # print("%d"%(var)) #- error num is req
# # print("%f"%(var)) #- error num is req
# print("%r"%(var)) #- '15'
# var = 15
# print("%x"%(var)) #- '15'
# print("%o"%(var)) #- '15'
# print("%d"%(var)) # - 15
# print("%f"%(var)) # - 15.000000
# # %[flags][width][.precision]type 
# print("hello:%2.2d world:%1d"%(123.45,123.456))
# # Python program showing how to use 
# # string modulo operator(%) to print 
# # fancier output 
# # print integer and float value 
# print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))  
# # print integer value 
# print("Total students : % 3d, Boys : % 2d" %(240, 120)) 
# # print octal value 
# print("% 7.3o"% (25))   
# # print exponential value 
# print("% 10.3E"% (356.08977)) 

# print("{} for {}".format(1,2))
# print("{1} for {0}".format(1,2))
# print("{0},{1},{some}".format(4,5,some = 3))


#---------------------------------------------------------------------------------------
#-----------------------------------strings-------------------------------------------------------
# str = "hello"
# str2 = '''
# world
# hi'''
# print(str2)





