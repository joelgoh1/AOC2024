# part 1
def main():
    with open('day7.csv') as f:
        data = f.read().split('\n')
    res = 0
    for i in range(len(data)):
        target, equation = data[i].split(':')
        target = int(target)
        equation = list(map(int, equation.split()))
        valids = []
        valids.append(target)
        for i in range(len(equation)-1, 0, -1):
            new_valids = []
            for j in valids:
                if j%equation[i] == 0 and j > 0:
                    new_valids.append(j // equation[i])
                if j > equation[i]:
                    new_valids.append(j-equation[i])
            valids = new_valids
        if len(valids) > 0 and equation[0] in valids:
            res += target
    return res

if __name__ == '__main__':
    print(main())

# part 2
def main():
    with open('day7.csv') as f:
        data = f.read().split('\n')
    res = 0
    for i in range(len(data)):
        target, equation = data[i].split(':')
        target = int(target)
        equation = list(map(int, equation.split()))
        valids = []
        valids.append(target)
        for i in range(len(equation)-1, 0, -1):
            new_valids = []
            for j in valids:
                temp = len(str(equation[i]))
                if len(str(j)) > temp and str(j)[-temp:] == str(equation[i]):
                    new_valids.append(int(str(j)[:-temp]))
                if j%equation[i] == 0 and j > 0:
                    new_valids.append(j // equation[i])
                if j > equation[i]:
                    new_valids.append(j-equation[i])
            valids = new_valids
        if len(valids) > 0 and equation[0] in valids:
            res += target
    return res

if __name__ == '__main__':
    print(main())