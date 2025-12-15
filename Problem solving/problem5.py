if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x1 = [a for a in range(x+1)]
    y1 = [a for a in range(y+1)]
    z1 = [a for a in range(z+1)]

    permutation = [[i, j, k] for i in x1 for j in y1 for k in z1]
    result = [res for res in permutation if sum(res) != n]
    
    print(result)
