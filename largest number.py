list1=[]
n=int(input("Enter the number of elements of the list: "))

for i in range(0,n):
    a=int(input())
    list1.append(a)
print(list1)

print("Largest number is: ",max(list1))
print("Smallest number is: ",min(list1))
