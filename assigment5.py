name=input("enter your name")
name1=name.count("a")
name2=name.count("e")
name3=name.count("i")
name4=name.count("o")
name5=name.count("u")
total_names=name1+name2+name3+name4+name5
count=len(name)
consonates=count-total_names
print(consonates)
print(total_names)  