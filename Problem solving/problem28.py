import cmath

if __name__ == "__main__":
    c = complex(input().strip())
    res = cmath.polar(c)
    print(res[0])
    print(res[1])