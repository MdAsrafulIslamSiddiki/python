def largest(a,b,c):
  largest_num=0
  if a>b:
    if a>c:
      largest_num=a
    else:
      largest_num=c
  else:
    if b>c:
      largest_num=b
    else:
      largest_num=c
  return largest_num

num1=int(input('Enter the number 1: ' ))
num2=int(input('Enter the number 2: ' ))
num3=int(input('Enter the number 3: ' ))

print("the largest number is", largest(num1,num2,num3))