# part 1
with open("day2.csv") as f:
    data = f.read().split("\n")

counter = 0
for line in data:
    line = list(map(int, line.split()))
    increase = line[0] < line[1]
    for i in range(1, len(line)):
        if increase:
            if line[i] < line[i-1]:
                break
        else:
            if line[i] > line[i-1]:
                break
        if abs(line[i] - line[i-1]) > 3:
            break
        if abs(line[i] - line[i-1]) < 1:
            break
    else:
        counter += 1
print(counter)

# part 2
with open("input.csv") as f:
    data = f.read().split("\n")

counter = 0
for line in data:
    line = list(map(int, line.split()))
    for i in range(len(line)):
        new_list = line.copy()
        new_list.pop(i)
        increase = new_list[0] < new_list[1]
        for i in range(1, len(new_list)):
            if increase:
                if new_list[i] < new_list[i-1]:
                    break
            else:
                if new_list[i] > new_list[i-1]:
                    break
            if abs(new_list[i] - new_list[i-1]) > 3:
                break
            if abs(new_list[i] - new_list[i-1]) < 1:
                break
        else:
            counter += 1
            break
print(counter)


# part 1
with open("day2.csv") as f:
    data = f.read().split("\n")

counter = 0
for line in data:
    line = list(map(int, line.split()))
    line = list(map(lambda x: line[x] - line[x-1], range(1, len(line))))
    if not (all(map(lambda x: x > 0, line)) or all(map(lambda x: x < 0, line))):
        continue
    if any(map(lambda x: abs(x) > 3, line)) or any(map(lambda x: abs(x) < 1, line)):
        continue
    counter +=1
#print(counter)

# part 2
# with open("day2.csv") as f:
#     data = f.read().split("\n")

# counter = 0
# for line in data:
#     line = list(map(int, line.split()))
#     line = list(map(lambda x: line[x] - line[x-1], range(1, len(line))))
#     cheat, cheat_index = False, 0
#     increase_count = []
#     decrease_count = []
#     for i in range(len(line)):
#         if line[i] < 0: 
#             decrease_count.append(i)
#         else:
#             increase_count.append(i)
#     if len(increase_count) > 1 and len(decrease_count) > 1:
#         continue
#     elif len(increase_count) > 1 and len(decrease_count) == 1:
#         cheat, cheat_index = True, decrease_count[0]
#     elif len(decrease_count) > 1 and len(increase_count) == 1:
#         cheat, cheat_index = True, increase_count[0]
#     if cheat:
#         if cheat_index > 0 and cheat_index < len(line) - 1:
#             line[cheat_index + 1] = line[cheat_index - 1] + line[cheat_index]
#         line.pop(cheat_index)
#         if any(map(lambda x: abs(x) > 3, line)) or any(map(lambda x: abs(x) < 1, line)):
#             continue
#     else:
#         for i in range(len(line)):
#             if abs(line[i]) > 3 or abs(line[i]) < 1:
#                 cheat, cheat_index = True, i
#         if cheat_index > 0 and cheat_index < len(line) - 1:
#             line[cheat_index + 1] = line[cheat_index - 1] + line[cheat_index]
#         line.pop(cheat_index)
#         if any(map(lambda x: abs(x) > 3, line)) or any(map(lambda x: abs(x) < 1, line)):
#             print(line)
#             continue
#     counter += 1

        
    
# print(counter)