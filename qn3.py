#if length of string is greater than 3 characters add ing as prefix else print same input
a = str(input("enter a word here: "))
if len(a) >3:
    print("I am",a+"ing")
else:
    print(a)