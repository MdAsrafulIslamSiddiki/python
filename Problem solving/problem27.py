from itertools import permutations
if __name__ == "__main__":
    n = list(map(str, input().split(' ')))
    input = n[0]
    counter = int(n[1])

    a =sorted(permutations(input, counter))
    for i in a:
        print(''.join(i))
    # print(n)
    # print(counter)