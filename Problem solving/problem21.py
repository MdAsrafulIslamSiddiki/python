def print_rangoli(size):
    for i in range(size):
        s = []
        s.extend([chr(c) for c in range(96+size, 96+size-i-1, -1)])
        s.extend([chr(c) for c in range(96+size, 96+size-i,-1)][::-1])
        print('-'.join(s).center(4*size-3,'-'))
    
    for i in range(size-2,-1,-1):
        s = []
        s.extend([chr(c) for c in range(96+size, 96+size-i-1, -1)])
        s.extend([chr(c) for c in range(96+size, 96+size-i,-1)][::-1])
        print('-'.join(s).center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)