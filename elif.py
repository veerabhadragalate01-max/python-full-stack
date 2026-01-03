# payments=input(" enter a payment mode")

# if payments=="phonepay":
#     print("intiating  phonepay transaction...")
# elif payments=="googlepay" :
#     print("intiatiating gpay trasaction")
# elif payments== "card":
#     print(" card payment")       
# else:
#     print(" not  supported")    

# user=input("enter a car name")
# print('''
#        1.TATA
#        2.MAHINDRA
#     ''')
# print(user)

# if user=="MAHINDRA":
#         print ('''
#                1.THAR
#                2.THAR ULTRA
#                3.MAHINDRA EV
#                 ''')
#         model=input(" enter a model")
#         if model=="THAR":
#             print("your have selected thar")
#         elif model=="THAR ULTRA":
#             print("your have selected THAR ULTRA")
#         elif model=="MAHINDRA EV":
#             print(" your have selected mhadra ev")    
#         else:
#             print("your slected car not there")
# # elif user=="TATA":
# #     print("you have slected tata car")
# # else:
# #     print("NOT SELECTED")                
atm=input('''please selecte input***:
      1.credit
      2.withdraw
      3.check balance
      ''')     
print('''
      1.credit
      2.withdraw
      3.check balance
      ''')
print(atm)
if atm=="credit":
    print('''
          1.enter amount
          2.enter your pin
          ''')      
    user=input("----*plese select the option*----;")
    if user=="enter amount":
        print("click yes to conform") 
    elif user=="enter your pin":
        print("plese enter to continue") 
    else:
        print("invalid input")
elif atm=="withdraw":
    print('''
          1.enter amount to withdraw
          2.enter the withdrawal pin
          ''')
    user2=input("enter amount to withdraw")
    if user2=="enter amount to withdraw":
        print("plese click to conform  amount:")
    elif user2=="enter the withdrawal pin":
        print("plese click to conform pin;")
    else:
        print(" invalid input")
elif atm=="check balance":
    print("amount in rupees--------")        
else:
    print("invalid option re enter or collect your card")