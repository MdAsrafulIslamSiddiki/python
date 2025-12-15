
print("Enter three number:")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("The largest number is: ",a)
elif a>b and a<c:
    print("The largest number is: ",c)
elif b>c:
    print("The largest number is: ",b)
else:
     print("The largest number is: ",c)