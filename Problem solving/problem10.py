if __name__ == "__main__":
    n = int(input())

    input_list = tuple(map(int, input().split()))

    print(hash(input_list))