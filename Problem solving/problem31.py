import calendar
weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print("------------Birth day name calculator--------------")
D = int(input('Enter the day of birth: '))
M = int(input('Enter the month of birth: '))
Y = int(input('Enter the year of birth: '))
# M,D,Y = map(int, input().split())
a=calendar.weekday(Y,M,D)
# print(weekdays[a])
print(a)