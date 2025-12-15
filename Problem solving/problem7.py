if __name__ == '__main__':
    records=[]
    second_gpa = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score]) 
    second_gpa=sorted(set([x[1] for x in records]))[1]
    result = sorted([y[0] for y in records if second_gpa == y[1]])
    
    for i in result:
        print(i)
