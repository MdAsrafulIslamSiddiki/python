print("-----------------------NUMBER CONVERSION-------------------------")
print("\n1.Binary to Decimal.")
print("2.Binary to Octal.")
print("3.Binary to Hexa-decimal.")
print("4.Decimal to Binary.")
print("5.Decimal to Octal.")
print("6.Decimal to Hexa-decimal.")
print("7.Octal to Binary.")
print("8.Octal to Decimal.")
print("9.Octal to Hexa-decimal.")
print("10.Hexa-decimal to Binary.")
print("11.Hexa-decimal to Decimal.")
print("12.Hexa-decimal to Octal.\n")

choice=int(input("Enter your choice: "))

if choice==1:
    n=input("Enter the binary number: ")
    for i in n:
        # print(i)