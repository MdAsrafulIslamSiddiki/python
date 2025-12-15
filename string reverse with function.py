def rev_string(str):
    index=len(str)
    rev_string=""
    
    while index>0:
        rev_string=rev_string+ str[index-1]
        index=index-1
    return rev_string

string=input('Enter the string: ')

print("The reverse of ", string,'is', rev_string(string))
