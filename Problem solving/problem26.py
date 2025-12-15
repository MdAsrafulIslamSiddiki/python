from collections import Counter

if __name__ == "__main__":
    n = int(input())
    stock = list(map(int, input().split(' ')))
    x = int(input())
    dictonary = Counter(stock)
    p=0
    
    for i in range(x):
        size, price = map(int, input().split(' '))
        
        if dictonary[size]:
            dictonary[size] -= 1
            p=p+price

    print(p)