"""#part 1

with open("day4input.txt", "r") as f:
    data = list(map(lambda x: list(map(lambda y:y.split("-"), x)) ,list(map(lambda x:x.replace("\n", "").split(","), f.readlines()))))

total = 0
for pairs in data:
    start1 = int(pairs[0][0])
    end1 = int(pairs[0][1])
    start2 = int(pairs[1][0])
    end2 = int(pairs[1][1])

    if start1 >= start2 and end1 <= end2:
        total += 1
        continue
    if start2 >= start1 and end2 <= end1:
        total += 1
        continue

print(total)"""

#part 2 

with open("day4input.txt", "r") as f:
    data = list(map(lambda x: list(map(lambda y:y.split("-"), x)) ,list(map(lambda x:x.replace("\n", "").split(","), f.readlines()))))

total = 0
for pairs in data:
    start1 = int(pairs[0][0])
    end1 = int(pairs[0][1])
    start2 = int(pairs[1][0])
    end2 = int(pairs[1][1])

    if max(end2, end1) - min(start1, start2) <= (end1-start1) + (end2-start2):
        total += 1

print(total)