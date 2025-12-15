def solve(s):
    l = s.split(" ")
    s = ''
    for i in l:
        s = s+i.capitalize()+' '
    return s
    
if __name__ == '__main__':

    s = input()

    result = solve(s)
