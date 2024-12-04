# part 1
import re

with open("day3.csv") as f:
    data = f.read()

res = 0
regex = r'mul\((\d+),(\d+)\)'
while True:
    search = re.search(regex, data)
    if not search:
        break
    match = search.group()
    end = search.end()
    match = list(map(int, match[4:-1].split(',')))
    res += match[0] * match[1]
    data = data[end:]
print(res)


# part 2
import re

with open("day3.csv") as f:
    data = f.read()

res = 0
regex_mul = r'mul\((\d+),(\d+)\)'
regex_do = r'do\(\)'
regex_dont = r'don\'t\(\)'
yes = True
while True:
    search_mul = re.search(regex_mul, data)
    search_do = re.search(regex_do, data)
    search_dont = re.search(regex_dont, data)
    if not search_mul and not search_do and not search_dont:
        break
    start_mul = search_mul.start() if search_mul else 10000000
    start_do = search_do.start() if search_do else 10000000
    start_dont = search_dont.start() if search_dont else 10000000

    if start_mul < start_do and start_mul < start_dont:
        match = search_mul.group()
        end = search_mul.end()
        match = list(map(int, match[4:-1].split(',')))
        if yes:
            res += match[0] * match[1]
    elif start_do < start_mul and start_do < start_dont:
        end = search_do.end()
        yes = True
    else: 
        end = search_dont.end()
        yes = False
    data = data[end:]
print(res)