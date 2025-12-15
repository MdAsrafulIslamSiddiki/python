def split_and_join(line):
    # write your code here
    line = line.split(" ")
    restult1 = "-".join(line)
    return restult1
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)