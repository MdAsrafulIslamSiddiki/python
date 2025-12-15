print("---------------DAY TO YEAR AND MONTH AND WEEK AND DAY CONVERTER---------------")

day=int(input("Enter the number of day: "))
year=day//365
year2=day%365
month=year2//30
days=year2%30
week=days//7
last_days=days%7

print("Conversion of ",day,"day = ",year,"year",month,"month and",week,"week and ",last_days,"days.")
