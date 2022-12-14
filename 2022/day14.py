"""
#part 1
with open("day14input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

rest = set()
maxY = 0
for line in data:
    points = list(map(lambda x:x.strip(), line.split("->")))
    for i in range(0, len(points)-1):
        x1, y1 = map(int, points[i].split(","))
        x2, y2 = map(int, points[i+1].split(","))
        maxY = max(maxY, max(y1, y2))
        if y2!=y1:
            for dy in range(min(y1, y2), max(y1, y2)+1):
                rest.add((x1, dy))
        else:
            for dx in range(min(x1, x2), max(x1, x2)+1):
                rest.add((dx, y1))

resting = True
res = 0
while resting:
    x = 500
    y = 0
    while True:
        if y > maxY:
            resting = False
            break
        if (x, y+1) not in rest:
            y += 1
        elif (x-1, y+1) not in rest:
            x -= 1
            y += 1
        elif (x+1, y+1) not in rest:
            x += 1
            y += 1
        else:
            rest.add((x,y))
            res += 1
            break

print(res)
"""
# part 2

with open("day14input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

rest = set()
maxY = 0
for line in data:
    points = list(map(lambda x:x.strip(), line.split("->")))
    for i in range(0, len(points)-1):
        x1, y1 = map(int, points[i].split(","))
        x2, y2 = map(int, points[i+1].split(","))
        maxY = max(maxY, max(y1, y2))
        if y2!=y1:
            for dy in range(min(y1, y2), max(y1, y2)+1):
                rest.add((x1, dy))
        else:
            for dx in range(min(x1, x2), max(x1, x2)+1):
                rest.add((dx, y1))

resting = True
res = 0
floor = maxY+2
while resting:
    x = 500
    y = 0
    while True:
        if y == floor-1:
            rest.add((x,y))
            res += 1
            break
        elif (x, y+1) not in rest:
            y += 1
        elif (x-1, y+1) not in rest:
            x -= 1
            y += 1
        elif (x+1, y+1) not in rest:
            x += 1
            y += 1
        else:
            if x == 500 and y == 0:
                resting = False
                res += 1
                break
            else:
                rest.add((x,y))
                res += 1
                break

print(res)