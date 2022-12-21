from collections import deque
with open("day18input.txt") as f:
    data = list(map(lambda x: tuple(map(int, x.strip().split(","))), f.readlines()))

maxX = 0
minX = 100
maxY = 0
minY = 100
maxZ = 0
minZ = 100

total = 0
for cube in data:
    x, y, z = cube
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    maxZ = max(maxZ, z)
    minX = min(minX, x)
    minY = min(minY, y)
    minZ = min(minZ, z)
    sides = 6
    for dx, dy, dz in [(0,0,-1),(0,0,1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]:
        if (x+dx, y+dy, z+dz) in data:
            sides -= 1
    total += sides
print("part 1:", total)

search = set()
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        for z in range(minZ, maxZ+1):
            if (x,y,z) not in data:
                search.add((x,y,z))


searched = set()
encased = set()
for s in search:
    if s in searched:
        continue
    q = deque()
    q.append(s)
    visited = set()
    trapped = True
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        x, y, z = cur
        if x > maxX or x < minX or y > maxY or y < minY or z > maxZ or z < minZ:
            trapped = False
            break
        for dx, dy, dz in [(0,0,-1),(0,0,1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]:
            next = (x+dx, y+dy, z+dz)
            if next not in data:
                if x+dx > maxX or x+dx < minX or y+dy > maxY or y+dy < minY or z+dz > maxZ or z+dz < minZ:
                    trapped = False
                    break
                q.append(next)
    for pos in visited:
        searched.add(pos)
    if trapped:
        for pos in visited:
            encased.add(pos)

for e in encased:
    x, y, z = e
    remove = 0
    for dx, dy, dz in [(0,0,-1),(0,0,1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]:
        if (x+dx, y+dy, z+dz) in data:
            remove += 1
    total -= remove

print("part 2:", total)