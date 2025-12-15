avg_number=int(input("Enter your Avg. Number :"))

if(avg_number>=80 and avg_number<=100):
    print("Your Grade = 'A+' ")

elif(avg_number>=70 and avg_number<=79):
    print("Your Grade = 'A' ")

elif(avg_number>=60 and avg_number<=69):
    print("Your Grade = 'A-' ")
    
elif(avg_number>=50 and avg_number<=59):
    print("Your Grade = 'B' ")
    

elif(avg_number>=40 and avg_number<=49):
    print("Your Grade = 'C' ")

elif(avg_number>=33 and avg_number<=39):
    print("Your Grade = 'D' ")
else:
    print("You have failed.")
    