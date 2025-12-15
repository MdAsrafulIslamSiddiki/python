a=int(input('enter the number: '))
sum=0
if a<0:
    print("Enter a positive number!")
else:
    for a in range(0,a+1):
       sum=sum+a
       a=a-1
print("The sum is: ",sum) 