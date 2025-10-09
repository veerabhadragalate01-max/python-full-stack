scretno=10
scret_no=int(input("enter your scret number"))
if scret_no==10:
    print("your guess correct")
elif scret_no<=7:
    print("your guess is too high")
elif scret_no<=5:
    print("your guess too low")
else:
    print("you guess incoorect")


