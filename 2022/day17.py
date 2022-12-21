with open("day17input.txt", "r") as f:
    jets = list(map(lambda x:x.split("\n")[0], f.readlines()))[0]


rocks = [[(0, 0), (1,0), (2,0), (3,0)], [(0, 1), (1, 0), (1,1), (1,2), (2,1)], [(0, 0), (1,0), (2,0), (2,1), (2,2)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1,0), (0, 1), (1,1)]]
rockN = 0
jetN = 0

tallest = -1

fallen = {(0,-1), (1,-1), (2,-1), (3,-1), (4,-1), (5,-1), (6,-1)}
seen = dict()

def pattern(tallest):
    global fallen
    pat = []
    for X,Y in fallen:
        if tallest-Y < 30:
            pat.append((X, tallest-Y))
    return frozenset(pat)
added = 0
while True:
    if rockN == 1000000000000:
        break
    if rockN == 2022:
        print(tallest+1+added)
    rock = rocks[rockN%len(rocks)]
    x = 2
    y = tallest + 4
    falling = True
    while falling:

        jet = jets[jetN%len(jets)]
        lastX = x
        if jet == ">":
            x += 1
        else:
            x -= 1
        for dx, dy in rock:
            if (x+dx, y+dy) in fallen or x+dx < 0 or x+dx > 6:
                x = lastX
                break

        y -= 1
        for dx, dy in rock:
            if (x+dx, y+dy) in fallen or y+dy == -1:
                y += 1
                falling = False
                break
        
        jetN += 1

    for dx, dy in rock:
        fallen.add((x+dx, y+dy))
        tallest = max(tallest, y+dy)
    
    newPattern = pattern(tallest)
    if (newPattern, jetN%len(jets), frozenset(rocks[rockN%len(rocks)])) in seen and rockN > 2022:
        oldT, oldRockN = seen[(newPattern, jetN%len(jets), frozenset(rocks[rockN%len(rocks)]))]
        dif = tallest-oldT
        rockDif = rockN-oldRockN
        amnt = (1000000000000-rockN)//rockDif
        rockN += amnt*rockDif
        added += amnt*dif

    seen[(newPattern, jetN%len(jets), frozenset(rocks[rockN%len(rocks)]))] = (tallest, rockN)


    
    rockN += 1

print(tallest+1+added)