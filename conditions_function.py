# name=input(" enter a name")
# day_state=input("state of day")
# def make_greeting(a,b):
#     x=f"good{day_state},{name}"
#     return x
   
# greeting=make_greeting(name, day_state)
# print(greeting)

# user_age=int(input("plese enter your age"))
# user_btechcgpa=float(input("enter your btechcgpa"))
# def is_eligible(a,b):
#     if a>18 and b>8:
#         return True
#     else:
#         return False
        

# result=is_eligible(user_age,user_btechcgpa)
# print(result)

# user=int(input(" enter a number"))

# def check_even_odd(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
        
# b=check_even_odd(user)
# print(b)

#calculation of bill
# menu={
#     "biryani":120,
#     "dal rice":70,
#     "meals":60,
#     "curdrice":80
#     }
# user_c1=input(" enter your oder:")
# user_q1=int(input("quntity required :"))
# BILL=user_q1*menu.get(user_c1)
# print(f"your bill is{BILL}")
cars={
    'skoda':{
        'kushaq':2,
        'octavia':3
    },
    'mahindra':{
        'Thar':8,
        'suv':16
    }
}
brand=input("enter a brand  name:")
model=input("enter model name:")
price=cars[brand][model]
print(f"your selected brand is {brand} and your car price is {price*100000}")
# cars = { 
#         'skoda': 
#             { 'kushaq': 20, 'Octavia': 30 },
            
#         'hyundai': 
            
#             { 'i10': 9, 'creta': 17 } , 
#         'mahindra':
            
#             { 'thar':14,
#              'xuv':32}
#         }
# brand=input("enter a brand  name:")
# model=input("enter model name:")
# price=cars[brand][model]
# print(price)