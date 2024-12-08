# part 1
import copy

def main():
    with open('day6.csv')  as f:
        data = f.read().split("\n")
    
    start = ()
    blockers = []
    visited = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                start = (i,j, "up")
                visited.add((i,j))
            if data[i][j] == "#":
                blockers.append((i,j))
    while True:
        i, j, pos = start
        col = list(filter(lambda x: x[1] == j, blockers))
        row = list(filter(lambda x: x[0] == i, blockers))
        if pos == "up":
            interest = list(filter(lambda x: x[0] < i, col))
            if not interest:
                for k in range(0, i):
                    visited.add((k, j))
                break
            max_i = max(interest, key = lambda x: x[0])[0]
            start = (max_i + 1, j, 'right')
            for k in range(max_i+1, i):
                visited.add((k, j))
        elif pos == 'down':
            interest = list(filter(lambda x: x[0] > i, col))
            if not interest:
                for k in range(i+1, len(data)):
                    visited.add((k, j))
                break
            min_i = min(interest, key = lambda x: x[0])[0]
            start = (min_i - 1, j, 'left')
            for k in range(i + 1, min_i):
                visited.add((k,j))

        if pos == 'right':
            interest = list(filter(lambda x: x[1] > j, row))
            if not interest:
                for k in range(j+1, len(data[0])):
                    visited.add((i, k))
                break
            min_j = min(interest, key = lambda x: x[1])[1]
            start = (i, min_j - 1, 'down')
            for k in range(j + 1, min_j):
                visited.add((i,k))
        if pos == "left":
            interest = list(filter(lambda x: x[1] < j, row))
            if not interest:
                for k in range(0, j):
                    visited.add((i, k))
                break
            max_j = max(interest, key = lambda x: x[1])[1]
            start = (i, max_j + 1, 'up')
            for k in range(max_j+1, j):
                visited.add((i, k))
    return len(visited) 
            
                
if __name__ == "__main__":
    print(main())


# part 2
def main():
    with open('day6.csv')  as f:
        data = f.read().split("\n")
    start = ()
    blockers = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                start = (i,j, "up")
            if data[i][j] == "#":
                blockers.append((i,j))
    
    def try_path(start, blockers):
        visited = set()
        overall_old = 0
        while True:
            new_square = False
            i, j, pos = start
            col = list(filter(lambda x: x[1] == j, blockers))
            row = list(filter(lambda x: x[0] == i, blockers))
            if pos == "up":
                interest = list(filter(lambda x: x[0] < i, col))
                if not interest:
                    return False
                max_i = max(interest, key = lambda x: x[0])[0]
                start = (max_i + 1, j, 'right')
                for k in range(max_i+1, i):
                    if (k,j) not in visited:
                        new_square = True
                    visited.add((k, j))
            elif pos == 'down':
                interest = list(filter(lambda x: x[0] > i, col))
                if not interest:
                    return False
                min_i = min(interest, key = lambda x: x[0])[0]
                start = (min_i - 1, j, 'left')
                for k in range(i + 1, min_i):
                    if (k,j) not in visited:
                        new_square = True
                    visited.add((k,j))
            if pos == 'right':
                interest = list(filter(lambda x: x[1] > j, row))
                if not interest:
                    return False
                min_j = min(interest, key = lambda x: x[1])[1]
                start = (i, min_j - 1, 'down')
                for k in range(j + 1, min_j):
                    if (i,k) not in visited:
                        new_square = True
                    visited.add((i,k))
            if pos == "left":
                interest = list(filter(lambda x: x[1] < j, row))
                if not interest:
                    return False
                max_j = max(interest, key = lambda x: x[1])[1]
                start = (i, max_j + 1, 'up')
                for k in range(max_j+1, j):
                    if (i,k) not in visited:
                        new_square = True
                    visited.add((i, k))
            if not new_square:
                overall_old += 1
                if overall_old == 4:
                    return True
            else:
                overall_old == 0
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in blockers:
                new_blockers = blockers + [(i, j)]
                if try_path(start, new_blockers):
                    res += 1
    return res

       
if __name__ == "__main__":
    print(main())