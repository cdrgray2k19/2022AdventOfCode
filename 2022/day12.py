"""
#part 1
from collections import deque
with open("day12input.txt", "r") as f:
    grid = list(map(lambda x:list(x.split("\n")[0]), f.readlines()))

start = None

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if grid[y][x] == "S":
            start = (y, x, 0)

def solve(start, grid):

    q = deque()
    q.append(start)
    x, y, dist = start
    visited = set()
    visited.add((y, x))
    while q:
        y, x, dist = q.popleft()
        val = grid[y][x]
        if val == "S":
            val = "a"

        for dy, dx in [(0, 1), (1,0), (-1, 0), (0, -1)]:
            if not(0<= y+dy < len(grid) and 0<= x+dx < len(grid[0])):
                continue
            new = grid[y+dy][x+dx]
            if new == "E":
                if val in ["z", "y"]:
                    print(y, x)
                    return dist+1
            else:
                if ord(new)-ord(val) <= 1 and (y+dy, x+dx) not in visited:
                    q.append((y+dy, x+dx, dist+1))
                    visited.add((y+dy, x+dx))

    return "no path found"

print(solve(start, grid))"""

#part 

from collections import deque
with open("day12input.txt", "r") as f:
    grid = list(map(lambda x:list(x.split("\n")[0]), f.readlines()))

end = None

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if grid[y][x] == "E":
            end = (y, x, 0)

def solve(end, grid):

    q = deque()
    q.append(end)
    x, y, dist = end
    visited = set()
    visited.add((y, x))
    while q:
        y, x, dist = q.popleft()
        val = grid[y][x]
        if val == "a" or val == "S":
            return dist
        if val == "E":
            val = 'z'

        for dy, dx in [(0, 1), (1,0), (-1, 0), (0, -1)]:
            if not(0<= y+dy < len(grid) and 0<= x+dx < len(grid[0])):
                continue
            new = grid[y+dy][x+dx]
            if new == "S":
                new = "a"
            if ord(val)-ord(new) <= 1 and (y+dy, x+dx) not in visited:
                q.append((y+dy, x+dx, dist+1))
                visited.add((y+dy, x+dx))

    return "no path found"

print(solve(end, grid))