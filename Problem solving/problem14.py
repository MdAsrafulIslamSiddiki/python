def mutate_string(string, position, character):
    # solution 1
    # l = list(string)
    # l[position] = character
    # string = ''.join(l)
    
    # solution 2
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)