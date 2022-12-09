"""
#part 1
with open("day9input.txt", "r") as f:
    moves = list(map(lambda x:x.split("\n")[0], f.readlines()))

def moveTail(head, tail):

    difx = head[0]-tail[0]
    dify = head[1]-tail[1]
    if abs(dify) <= 1 and abs(difx) <= 1:
        return tail
    
    if dify == 0:
        tail[0] += difx/abs(difx)
    elif difx == 0:
        tail[1] += dify/abs(dify)
    else:
        tail[0] += difx/abs(difx)
        tail[1] += dify/abs(dify)

    return tail


visited = set()
head = [0,0]
tail = [0,0]
visited.add(tuple(tail))
for m in moves:
    m = m.split()
    for i in range(0, int(m[1])):
        #update head
        if m[0] == "U":
            head[1] += 1
        elif m[0] == "D":
            head[1] -= 1
        elif m[0] == "R":
            head[0] += 1
        else:
            head[0] -= 1
        #figure out if its needs to move
        tail = moveTail(head, tail)
        visited.add(tuple(tail))

print(len(visited))"""

#part 2

with open("day9input.txt", "r") as f:
    moves = list(map(lambda x:x.split("\n")[0], f.readlines()))

def moveTail(head, tail):

    difx = head[0]-tail[0]
    dify = head[1]-tail[1]
    if abs(dify) <= 1 and abs(difx) <= 1:
        return tail
    
    if dify == 0:
        tail[0] += difx/abs(difx)
    elif difx == 0:
        tail[1] += dify/abs(dify)
    else:
        tail[0] += difx/abs(difx)
        tail[1] += dify/abs(dify)

    return tail


visited = set()
knots = []
for i in range(0, 10):
    knots.append([0,0])
visited.add(tuple(knots[-1]))
for m in moves:
    m = m.split()
    for i in range(0, int(m[1])):
        #update head
        if m[0] == "U":
            knots[0][1] += 1
        elif m[0] == "D":
            knots[0][1] -= 1
        elif m[0] == "R":
            knots[0][0] += 1
        else:
            knots[0][0] -= 1
        #figure out if its needs to move
        for i in range(1, len(knots)):
            knots[i] = moveTail(knots[i-1], knots[i])
            
        visited.add(tuple(knots[-1]))

print(len(visited))