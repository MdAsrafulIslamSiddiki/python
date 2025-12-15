from itertools import product

if __name__ == "__main__":
    A = [int(item) for item in input("Enter the list items : ").split()]
    B = [int(item) for item in input("Enter the list items : ").split()]



    # result = [(a,b) for a in A for b in B]


    for i in product(A, B):
        print (i, end=' ')