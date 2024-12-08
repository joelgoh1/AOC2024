# part 1
def main():
    with open('day8.csv') as f:
        data = f.read().split('\n')
    
    ds = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            interest = data[i][j]
            if interest != '.':
                if interest not in ds:
                    ds[interest] = []
                ds[interest].append((i, j))
    res = set()
    for k, v in ds.items():
        if len(v) >= 2:
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    diff_i = abs(v[i][0] -v[j][0])
                    diff_j = abs(v[i][1] - v[j][1])
                    possible_is = [max(v[i][0], v[j][0]) + diff_i, min(v[i][0], v[j][0]) - diff_i]
                    possible_js = [max(v[i][1], v[j][1]) + diff_j, min(v[i][1], v[j][1]) - diff_j]
                    if v[i][1] < v[j][1]:
                        if possible_is[1] >= 0 and possible_js[1] >= 0:
                            res.add((possible_is[1], possible_js[1]))
                        if possible_is[0] < len(data) and possible_js[0] < len(data):
                            res.add((possible_is[0], possible_js[0]))
                    else:
                        if possible_is[1] >= 0 and possible_js[0] < len(data[0]):
                            res.add((possible_is[1], possible_js[0]))
                        if possible_is[0] < len(data) and possible_js[1] >= 0:
                            res.add((possible_is[0], possible_js[1]))
    return len(res)

if __name__ == '__main__':
    print(main())


# part 2
def main():
    with open('day8.csv') as f:
        data = f.read().split('\n')
    
    ds = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            interest = data[i][j]
            if interest != '.':
                if interest not in ds:
                    ds[interest] = []
                ds[interest].append((i, j))
    res = set()
    for k, v in ds.items():
        if len(v) >= 2:
            for i in range(len(v)):
                res.add(v[i])
                for j in range(i+1, len(v)):
                    diff_i = abs(v[i][0] -v[j][0])
                    diff_j = abs(v[i][1] - v[j][1])
                    possible_is = [max(v[i][0], v[j][0]) + diff_i, min(v[i][0], v[j][0]) - diff_i]
                    possible_js = [max(v[i][1], v[j][1]) + diff_j, min(v[i][1], v[j][1]) - diff_j]
                    if v[i][1] < v[j][1]:
                        while True:
                            if possible_is[1] >= 0 and possible_js[1] >= 0:
                                res.add((possible_is[1], possible_js[1]))
                                possible_is[1] -= diff_i 
                                possible_js[1] -= diff_j
                            else:
                                break
                        while True:
                            if possible_is[0] < len(data) and possible_js[0] < len(data):
                                res.add((possible_is[0], possible_js[0]))
                                possible_is[0] += diff_i
                                possible_js[0] += diff_j
                            else:
                                break
                    else:
                        while True:
                            if possible_is[1] >= 0 and possible_js[0] < len(data[0]):
                                res.add((possible_is[1], possible_js[0]))
                                possible_is[1] -= diff_i
                                possible_js[0] += diff_j
                            else:
                                break
                        while True:
                            if possible_is[0] < len(data) and possible_js[1] >= 0:
                                res.add((possible_is[0], possible_js[1]))
                                possible_is[0] += diff_i
                                possible_js[1] -= diff_j
                            else:
                                break
    return len(res)

if __name__ == '__main__':
    print(main())