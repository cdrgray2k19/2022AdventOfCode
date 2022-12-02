"""
#part 1
with open("day2input.txt", "r") as f:    
    data = list(map(lambda x: x.replace("\n", "").split(), f.readlines()))

oppositionMoves = {"A": 1, "B": 2, "C": 3}
ownMoves = {"X": 1, "Y": 2, "Z": 3}

total = 0
for round in data:
    score = 0
    opposition = round[0]
    own = round[1]
    score += ownMoves[own]
    diff = ownMoves[own] - oppositionMoves[opposition]
    if diff in [1, -2]:
        score += 6
    elif diff == 0:
        score += 3
    total += score

print(total)"""


#part 2
with open("day2input.txt", "r") as f:    
    data = list(map(lambda x: x.replace("\n", "").split(), f.readlines()))

oppositionMoves = {"A": 1, "B": 2, "C": 3}

total = 0
for round in data:
    score = 0
    opposition = round[0]
    result = round[1]
    
    if result == "X":
        own = oppositionMoves[opposition] - 1
        if own == 0:
            own = 3
        score += own
    elif result == "Y":
        own = oppositionMoves[opposition]
        score += own + 3
    else:
        own = oppositionMoves[opposition] + 1
        if own == 4:
            own = 1
        score += own + 6
    total += score

print(total)