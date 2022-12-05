"""
#part 1
from textwrap import wrap
stacks = []
start = 0
with open("day5input.txt", "r") as f:
    data = f.readlines()
    for i in range(0, len(data)):
        if data[i] == "\n":
            start = i+1
            for _ in range(0, max(list(map(int, data[i-1].split())))):
                stacks.append([])
            for j in range(i-2, -1, -1):
                line = wrap(data[j], 4, drop_whitespace=False)
                processed = list(map(lambda x:x.replace(" ", "").replace("]", "").replace("[", ""),  line))
                for k in range(0, len(processed)):
                    if processed[k] != "":
                        stacks[k].append(processed[k])
for i in range(start, len(data)):
    if data[i] == "\n":
        continue
    line = list(map(int, data[i].replace("\n", "").replace("move", "").replace("start", "").replace("from", "").replace("to", "").split()))
    for _ in range(0, line[0]):
        temp = stacks[line[1]-1].pop()
        stacks[line[2]-1].append(temp)

msg = ""
for i in range(0, len(stacks)):
    msg += stacks[i][-1]

print(msg)"""

#part 2

from textwrap import wrap
stacks = []
start = 0
with open("day5input.txt", "r") as f:
    data = f.readlines()
    for i in range(0, len(data)):
        if data[i] == "\n":
            start = i+1
            for _ in range(0, max(list(map(int, data[i-1].split())))):
                stacks.append([])
            for j in range(i-2, -1, -1):
                line = wrap(data[j], 4, drop_whitespace=False)
                processed = list(map(lambda x:x.replace(" ", "").replace("]", "").replace("[", ""),  line))
                for k in range(0, len(processed)):
                    if processed[k] != "":
                        stacks[k].append(processed[k])


for i in range(start, len(data)):
    if data[i] == "\n":
        continue
    line = list(map(int, data[i].replace("\n", "").replace("move", "").replace("start", "").replace("from", "").replace("to", "").split()))
    temp = stacks[line[1]-1][-line[0]:]
    stacks[line[1]-1] = stacks[line[1]-1][:-line[0]]
    stacks[line[2]-1] += temp

msg = ""
for i in range(0, len(stacks)):
    msg += stacks[i][-1]

print(msg)