"""
#part 1
import re

with open("day15input.txt", "r") as f:
    data = list(map(lambda x:x.split('\n')[0], f.readlines()))

noB = set()
Y = 2000000
for line in data:
    sx, sy, bx, by = map(int,re.findall("-?\d*\.{0,1}\d+", line))
    d = abs(bx-sx) + abs(by-sy)
    distY = abs(Y-sy)
    if distY <= d and (sx, Y) != (bx, by):
        for i in range(0, d-distY+1):
            if (sx+i, Y) != (bx, by):
                noB.add((sx+i, Y))
            if (sx-i, Y) != (bx, by):
                noB.add((sx-i, Y))

print(len(noB))
"""
#part 2
import re 
import time

start = time.time()

with open("day15input.txt", "r") as f:
    data = list(map(lambda x:x.split('\n')[0], f.readlines()))

out = set()

sensors = []
dists = []
def outAdd(x, y):
    global out
    global sensors
    global dists
    if not(0 <= x <= 4000000 and 0 <= y <= 4000000):
        return
    for i in range(0, len(sensors)):
        sx, sy = sensors[i]
        d = abs(x-sx) + abs(y-sy)
        if d<=dists[i]:
            return
    global start
    print(x*4000000 + y)
    end = time.time()
    print(end-start)
    assert False

for line in data:
    sx, sy, bx, by = map(int,re.findall("-?\d*\.{0,1}\d+", line))
    d = abs(bx-sx) + abs(by-sy)
    sensors.append((sx, sy))
    dists.append(d)


for i in range(0, len(sensors)):
    sx, sy = sensors[i]
    d = dists[i]
    for i in range(0, d+2):
        outAdd(sx - d - 1 - i, sy+i)
        outAdd(sx + d + 1 - i, sy+i)
        outAdd(sx - d - 1 - i, sy-i)
        outAdd(sx + d + 1 - i, sy-i)