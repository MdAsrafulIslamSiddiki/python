print("Prime Number from 1 to 100: ")
for num in range (1,101):
    flag=False
    
    for i in range(2,num):
        if num % i==0:
            flag=True
            break
    if flag==False:
        print(num,end="  ")