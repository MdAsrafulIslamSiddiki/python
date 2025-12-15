n=int(input("Enter the number: "))
if n<0:
    print("Please enter a positive number")
else:
    print("The even numbers of 1 to {0}: " .format(n))
    for x in range(2,n+1,2):
        print(x)
