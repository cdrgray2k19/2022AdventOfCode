"""
#part 1
with open("day8input.txt", "r") as f:
    data = list(map( lambda x:list(map( lambda x:int(x), list(x.split("\n")[0]))), f.readlines()))

#create left, right, up, down arrays
left = []
right = []
up = []
down = []

empty = []
for _ in range(0, 10):
    empty.append(0)

for _ in range(0, len(data)):
    left.append(empty.copy())
    right.append(empty.copy())
    up.append(empty.copy())
    down.append(empty.copy())

#traverse and make arrays
for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        num = data[y][x]
        if x not in [0, len(data[0])-1]:
            if y == 0:
                up[x][num] += 1
            else:
                down[x][num] += 1
        if y not in [0, len(data[0])-1]:
            if x == 0:
                left[y][num] += 1
            else:
                right[y][num] += 1

def getMax(arr):
    for i in range(9, -1, -1):
        if arr[i] != 0:
            return i


#now traverse and look for visible, updating arrays as we go along

visible = (len(data)**2)-((len(data)-2)**2)

for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        num = data[y][x]
        right[y][num] -= 1
        down[x][num] -= 1
        trees = []
        trees.append(getMax(left[y]))
        trees.append(getMax(right[y]))
        trees.append(getMax(up[x]))
        trees.append(getMax(down[x]))
        for t in trees:
            if t < num:
                visible += 1
                break
        left[y][num] += 1
        up[x][num] += 1

print(visible)"""

#part 2

from collections import deque

with open("day8input.txt", "r") as f:
    data = list(map( lambda x:list(map( lambda x:int(x), list(x.split("\n")[0]))), f.readlines()))

#create left, right, up, down arrays
left = []
right = []
up = []
down = []

empty = []
for _ in range(0, 10):
    q = deque()
    empty.append(q.copy())

for _ in range(0, len(data)):
    empty = []
    for _ in range(0, 10):
        new = deque()
        empty.append(new)
    left.append(empty.copy())

for _ in range(0, len(data)):
    empty = []
    for _ in range(0, 10):
        new = deque()
        empty.append(new)
    right.append(empty.copy())
for _ in range(0, len(data)):
    empty = []
    for _ in range(0, 10):
        new = deque()
        empty.append(new)
    down.append(empty.copy())

for _ in range(0, len(data)):
    empty = []
    for _ in range(0, 10):
        new = deque()
        empty.append(new)
    up.append(empty.copy())
#traverse and make arrays
#under each index, store queue of positions of that height of tree, at start of right and down,  are the closer trees for that height, at end of left and up, are the closer trees for that height
for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        num = data[y][x]
        
        down[x][num].append(y)

        right[y][num].append(x)

def getDist(arr, height, pos, max):
    seen = []
    for i in range(9, height-1, -1):
        if len(arr[i]) == 0:
            seen.append(abs(max-pos))
            continue
        seen.append(abs(pos-arr[i][0]))
    return min(seen)


#now traverse and look for visible, updating arrays as we go along

maxScenic = -1

for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        tree = data[y][x]
        #for each direction look for closest tree that is taller or the same height as the tree
        right[y][tree].popleft()
        down[x][tree].popleft()
        distances = []
        distances.append(getDist(left[y], tree, x, 0))
        distances.append(getDist(right[y], tree, x, len(data[0])-1))
        distances.append(getDist(up[x], tree, y, 0))
        distances.append(getDist(down[x], tree, y, len(data)-1))
        left[y][tree].appendleft(x)
        up[x][tree].appendleft(y)
        scenic = 1
        for d in distances:
            scenic *= d
        if scenic > maxScenic:
            maxScenic = scenic

print(maxScenic)