height=int(input("Enter your height:"))

bill=100
if height>=120:
    age=int(input("Enter your age:"))
    photo=input("You can take photo?\n")
    if age<=12:
        if photo=="yes":
            bill=bill+5+3
            print("The total bill is=",bill)
        else:
            bill=bill+5
            print("The total bill is=",bill)
    elif age>12 and age<18:
        if photo=="yes":
            bill=bill+7+3
            print("The total bill is=",bill)
        else:
            bill=bill+7
            print("The total bill is=",bill)
    else:
        if photo=="yes":
            bill=bill+12+3
            print("The total bill is=",bill)
        else:
            bill=bill=12
            print("The total bill is=",bill)
else:
    print("you can't ride.")

