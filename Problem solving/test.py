def print_formatted(number):
    l = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{len}d} {0:{len}o} {0:{len}X} {0:{len}b}".format(i, len = l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)