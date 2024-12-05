# part 1
def main():

    with open('day5.csv')  as f:
        data = f.read().split("\n")
    nodes = {}
    res = 0
    for line in data:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if x not in nodes:
                nodes[x] = []
            if y not in nodes:
                nodes[y] = []
            nodes[y].append(x)
        else:
            if line:
                line = list(map(int, line.split(',')))
                for i in range(len(line)):
                    valid = True
                    for j in range(i+1, len(line)):
                        if line[i] in nodes and line[j] in nodes[line[i]]:
                            valid = False
                            break
                    if not valid:
                        break
                else:
                    res += line[(len(line) - 1)//2]
    return res
            
                
if __name__ == "__main__":
    print(main())


# part 2
def main():
    with open('day5.csv')  as f:
        data = f.read().split("\n")
    
    def check_valid(line, nodes):
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i] in nodes and line[j] in nodes[line[i]]:
                    return False, i, j
        return True, 0, 0

    def fix(line, nodes, i, j):
        a = line.pop(j)
        line.insert(max(0, i-1), a)
        validity = check_valid(line, nodes)
        print(a, validity, line)
        if validity[0]:
            return line
        else:
            return fix(line, nodes, validity[1], validity[2])



    nodes = {}
    res = 0
    for line in data:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if x not in nodes:
                nodes[x] = []
            if y not in nodes:
                nodes[y] = []
            nodes[y].append(x)
        else:
            if line:
                line = list(map(int, line.split(',')))
                for i in range(len(line)):
                    valid = True
                    for j in range(i+1, len(line)):
                        if line[i] in nodes and line[j] in nodes[line[i]]:
                            line = fix(line, nodes, i, j)
                            valid = False
                            break
                    if not valid:
                        print(line)
                        res += line[(len(line) - 1)//2]
                        break
    return res
            
                
if __name__ == "__main__":
    print(main())