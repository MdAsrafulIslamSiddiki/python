import math
print("Enter the heights of the sides of triangle: ")
a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and a+c>b:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area  of the triangle: ",area)
else:
    print("The triangle is not possible.")