#multiple inheritance 
# class car:
#     def __init__(self,name):
#         print(name)
# class bmw(car):
#     def __init__(self,name,model):
#         super().__init__(name)
#         print("bmw model:",model)
# class maruthi(car):
#     def __init__(self,name,model):
#         super().__init__(name)
#         print("maruthi model:",model)
# c = bmw("car","x20")
# x = maruthi(" car"," u5000")

#multilevel inheritance 

# class a:
#     def __init__(self,var_a):
#         print("from a",var_a)
#     def fun(self):
#         print("123")
# class b(a):
#     def __init__(self,var_a,var_b):
#         super().__init__(var_a)
#         print("from b",var_b)
# class c(b):
#     pass
#     def __init__(self, var_a, var_b, var_c):
#         super().__init__(var_a, var_b)
#         print("from c",var_c)
#         super().fun()
# c1 = c(1,2,3)


#multiple inheritance
#more than one parent class 


class father:
    def __init__(self):
        print("from father")
class mother:
    def __init__(self):
        print("from mother")
class son(father,mother):
    def __init__(self):
        super().__init__()
        print("from son")

son1 = son()
