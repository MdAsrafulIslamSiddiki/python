a=float(input("Enter your weight:"))
b=float(input("Enter your hight:"))
c= a/b**b
print("Your BMI is ",c)
if c<18.5 :
    print("You are underweight.")
elif c<25 and c>18.5 :
    print("You have a normal weight.")
elif c<30 and c>25 :
    print("You have over weight.")
elif c<35 and c>30 :
    print("You are obese. ")
elif c>35:
    print("You are clinically obese.")
