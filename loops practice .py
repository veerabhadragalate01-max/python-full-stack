# for i in range(11,16):
#     print(i)

# num=7
# for i in range(6):
#     n=int(input(" enter a number :"))
#     if n>=num:
#         print('correct')
#     else:
#         print('try again')

# person={
#     'name':'',
#     'age':0,
#     'gender':''
# }

# for key in person:
#     i= input(f'enter a your{key}:')
#     person[key]= i

# print(person)
    
# fruits={
#     'mango':34,
#     'cherry':10,
#     'banana':7,
#     'dragon':25
# }
# for i in fruits:
#     user=input(f"enter upadted price of {valuve} :")
#     fruits[valuve]=user
# print(fruits)
products= [
    
          {'name':'laptop', 'price':1200},
          {'name':'headphones', 'price':150},
          {'name':'desk chai', 'price':250},
          {'name':'smart watch', 'price':300},
          ]
price=0
for i in products:
     price += i['price']
     
print(price)