#strings

# str = "karthi"
# print(str[0])
# print(str[-1])
# print(str[-2:-5:-1])
# print(str[-2:-5:-1]+str[1:4])
#str[2] = "p" -- we cannot update string it gives error
#del str[2] -- this also gives error we cannot delete string
#print("i'm \"karthik\"") --escape sequencing
# print("C:\\Python\\Geeks\\")
# print(r"I'm a \"Geek\"")
# print(r"I'm a "Geek"")
# print(r"C:\\Python\\Geeks\\")# --to print raw string

#string formatting
# print("{} hello {} hi".format(1,"hey"))
# print("{0} hello {1} hi".format(1,"hey"))
# print("{first} hello {second} hi".format(first=1,second="hey"))

#logical operator in string

# print("hello" and "hi") # if none of them is empty string then returns second string
# print("hello" or "hi")# if none of them is empty string then returns first string
# print("hi" or "") # if one them are empty  but one is a string then returns that string
# print("hello" and "") #both should be string returns empty string
# print(not "hello") #false
# print(not "") #true


# def power(a, b): 
#     """Returns arg1 raised to power arg2."""
   
#     return a*b 
  
# print(power.__doc__ )

# different ways for reversing string

# def rev1(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str

# #using recursion

# def rev2(s):
#     if len(s) == 0:
#         return s
#     else:
#         return rev2(s[1:])+s[0]

# #most easy method

# def rev3(s):
#     str = s[::-1]
#     return str

# #using reversed method 
# #reversed method returns an iterator
# #join used for joining iterables with a string
# def rev4(s):
#     return "".join(reversed(s))

# print(rev1("karthik"))
# print(rev2("karthik"))
# print(rev3("karthik"))
# print(rev4("karthik"))


# #palindrome program
# def palindrome(s):
#     if(s == s[::-1]):
#         print("yes")
#     else:
#         print("no")
# palindrome("malayalam")

str  = "hello"
str += " world"
print(str)

print("we " + "can " + "concatinate ")


