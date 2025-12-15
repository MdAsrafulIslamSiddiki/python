n=int(input("Enter the last number of "))
print("2+4+6+....+",n*2)
sum=0
for i in range(2,n*2+1,2):
    sum=sum+i
print("The summation of the series = ",sum)