# part 1
with open("data.csv") as f:
    data = f.read().split("\n")

ls1, ls2 = [], []

for line in data:
    x, y = line.split()
    ls1.append(int(x))
    ls2.append(int(y))

ls1.sort()
ls2.sort()

print(sum(list(map(lambda x: abs(ls1[x] - ls2[x]), range(len(ls1))))))

# part 2
with open("data.csv") as f:
    data = f.read().split("\n")

ls1, ds = [], {}

for line in data:
    x, y = line.split()
    ls1.append(int(x))
    y = int(y)
    if y not in ds:
        ds[y] = 0
    ds[y] +=1


print(sum(list(map(lambda x: ls1[x] * ds.get(ls1[x], 0), range(len(ls1))))))