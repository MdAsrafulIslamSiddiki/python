def fectorial(n):
    if n==1:
        return 1
    else:
        return n*fectorial(n-1)

x=int(input("Enter the number: "))
print("the factorial of ",x,"is",fectorial(x))