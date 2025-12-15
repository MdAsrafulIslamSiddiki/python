salary = int(input("Enter your salary: "))
year = int(input("Enter the year of services: "))
if(year>10):
    bonus = (salary *10)/100
    print("Your bonus is: ",round(bonus))
elif(year>=6):
    bonus = (salary *8)/100
    print("Your bonus is: ",round(bonus))
else:
    bonus = (salary *5)/100
    print("Your bonus is: ",round(bonus))