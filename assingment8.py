#°C = (°F - 32) × 5/9
#°C = (°F - 32) × 5/9
#F = (C × 9/5) + 32
temp=float(input("enter the temparature="))
unit=input("enter clesius or fahrenheit use (c/f):")
if unit=="c":
    Fahrenheit=(temp*9/5) + 32
    print("temparature in fahrenheit",Fahrenheit)
elif unit=="f":
    celsius=(temp-32)*5/9
    print("temp in celsius",celsius)
else:
    print("invalid input please give c or f ")

#Fahrenheit=(temp*9/5) + 32
    # print("temparature in fahrenheit",Fahrenheit)
    # celsius=(temp-32)*5/9
    # print("temp in celsius",celsius)

