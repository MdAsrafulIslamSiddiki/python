number=int(input("Enter the number: "))
fact=1

if number==0:
  print("The factorial of 0 is 1.")
elif number==1:
  print("The factorial of 1 is 1.")
else:
  for i in range (1,number+1):
    fact=fact*i
  print('The factorial of', number, 'is',fact)
    