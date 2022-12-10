"""
#part 1
with open("day10input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

def checkCycle(cycle, val):
    if (cycle-20)%40 == 0:
        return cycle*val
    return 0


res = 0
cycle = 0
val = 1
for line in data:
    if line == "noop":
        cycle += 1
        res += checkCycle(cycle, val)
    else:
        line = line.split()
        cycle += 1
        res += checkCycle(cycle, val)
        cycle += 1
        res += checkCycle(cycle, val)
        val += int(line[1])

print(res)"""

#part 2

with open("day10input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

def update(cycle, pos):
    global draw
    cycle -= 1
    col = cycle%40
    row = cycle//40
    if abs(col-pos) <= 1:
        draw[row][col] = "#"
    
global draw
draw = []
for i in range(0, 6):
    new = []
    for i in range(0, 40):
        new.append(".")
    draw.append(new)


cycle = 0
pos = 1
for line in data:
    if line == "noop":
        cycle += 1
        update(cycle, pos)
    else:
        line = line.split()
        cycle += 1
        update(cycle, pos)
        cycle += 1
        update(cycle, pos)
        pos += int(line[1])

for i in range(0, 6):
    print(draw[i])