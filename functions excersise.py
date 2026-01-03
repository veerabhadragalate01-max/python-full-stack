#functioons
##a function is a reusable block of code that perform specfic task
# code reusability, modularity ,abstracdtion organization
# functions names as verbs, varible names as nouns
# () is important while declaring function

# def print_till3():
#     print(1)
#     print(2)
#     print(3)
# def print_till4():
#     print(1)
#     print(2)
#     print(3)
#     print(4)
# def print_till2():
#     print(1)
#     print(2)
#     print(3)
# print("staring")
# print_till2()
# print_till3()  
# print_till4()  
# print("ending")
    
# name=input('enter your name:')
# place=input('enter your city')
# age=int(input("emter your age:"))
# def write(a,b,c):
#     if b=="hyd":
#         print(f"hello{a},are you from   {b}?  and what is your age{c}")
#     else:
#         print("invalid input")
# write(name,place,age)        

no1=int(input("enter a number1:"))
no2=int(input("enter a number2:"))
def multiply(a,b):
    print(f"The multiplication of{a*b}")
def subtraction(a,b):
    print(f"The subraction of{a-b}")
    
def divison(a,b):
    print(f"The division of{a/b}")
multiply(no1,no2)
subtraction(no1,no2)
divison(no1,no2)