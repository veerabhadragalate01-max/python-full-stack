
lst=[]
def swap_case(user):
 for char in user:
    if char.islower():
        lst.append(char.upper())
    elif char.isupper():
        lst.append(char.lower())
    else:
        lst.append(char)
 return "".join(lst)
user=input("enter a word")
print(swap_case(user))

a=input("enter your input")
b=a.swapcase()
print(b)