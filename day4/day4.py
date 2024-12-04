# part 1
with open('day4.csv') as f:
    data = f.read().split("\n")

def transpose(mat):
    return list(map(lambda x: ''.join(x), zip(*mat)))

def countDiag(mat):
    counter = 0
    search = ["XMAS", "SAMX"]
    if mat[0][0] + mat[1][1] + mat[2][2] + mat[3][3] in search:
        counter += 1
    if mat[0][3] + mat[1][2] + mat[2][1] + mat[3][0] in search:
        counter += 1
    return counter

def countRow(data):
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[0])-3):
            row = data[i][j:j+4]
            if row == "XMAS" or row == "SAMX":
                counter += 1
    return counter

counter = 0
counter += countRow(data)
counter += countRow(transpose(data))
for i in range(len(data)-3):
    for j in range(len(data[0])-3):
        mat = list(map(lambda x: x[j:j + 4], data[i:i + 4]))
        counter += countDiag(mat)
print(counter)

# part 2
with open('day4.csv') as f:
    data = f.read().split("\n")


def countDiag(mat):
    counter = 0
    search = ["MAS", "SAM"]
    if mat[0][0] + mat[1][1] + mat[2][2] in search and \
        mat[0][2] + mat[1][1] + mat[2][0]  in search:
        counter += 1
    return counter


counter = 0
for i in range(len(data)-2):
    for j in range(len(data[0])-2):
        mat = list(map(lambda x: x[j:j + 3], data[i:i + 3]))
        counter += countDiag(mat)
print(counter)