a = input("Enter something: ")

digit = special_charecter = 0
a_length = len(a)
for i in range(0,a_length):
    if(a[i] >= '0' and a[i] <='4.00'):
        digit+=1
    
    else:
        special_charecter+=1
print("aphabets no: ",digit)
print("special charecters: ",  special_charecter)
