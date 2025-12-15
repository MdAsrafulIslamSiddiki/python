num = int(input("Enter the terms: "))
n=0
i=0
while n<num:
    i+=1
    flag=1
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
    
    if flag==1:
        print(i,end=' ')
        n+=1