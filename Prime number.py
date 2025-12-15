a=int(input("Enter a number :"))
for x in range(2,a,10):
  if a%x!=0:
    print("The number is prime number.")
    break
else:
  print("the number is not prime number.")
