str=input('Enter a string: ')

index=len(str)
rev_string=" "

while index>0:
    rev_string= rev_string + str[index - 1]
    index=index-1
print("The reverse string is: ", rev_string)