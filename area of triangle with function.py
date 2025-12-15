import math
def triangle(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b :
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        print("The value of arms can't create a triangle")
    return area

arm1=int(input("Enter the arm 1: "))
arm2=int(input("Enter the arm 2: "))
arm3=int(input("Enter the arm 3: "))
print("The area of triangle is",triangle(arm1,arm2,arm3))
