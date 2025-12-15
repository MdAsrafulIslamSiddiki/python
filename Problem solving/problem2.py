if __name__ == '__main__':
    n = int(input())
    if n>20:
        print("n is out of range.")
    else:
        for i in range(n):
            print(i*i)