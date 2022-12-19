from functools import lru_cache
with open("day16input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

flow = dict()
paths = dict()
index = dict()

count = 1
for line in data:
    name = line.split()[1]
    line = line.split(";")
    num = line[0].split("=")[1]
    tunnels = list(map(lambda x:x.replace(",",""), line[1].split("valve")[1].split()))
    if tunnels[0] == "s":
        tunnels.pop(0)
    index[name] = count
    flow[name] = int(num)
    paths[name] = tunnels
    count += 1

seen = dict()


#@lru_cache(maxsize=None)
def solve(pos, time, open, players):

    ans = 0
    global seen
    if (pos, time, open, players) in seen:
        return seen[(pos, time, open, players)]
    if time == 0:
        if players == 0:
            return 0
        return solve("AA", 26, open, 0)
    global flow
    global paths
    global index

    if flow[pos] > 0 and (open & (2<<index[pos])) == 0:
        temp = open | (2<<index[pos])
        ans = max(ans, (flow[pos]*(time-1)) + solve(pos, time-1, temp, players))
    for newPos in paths[pos]:
        ans = max(ans, solve(newPos, time-1, open, players))
    seen[(pos, time, open, players)] = ans
    return ans


print("part 1: ", solve("AA", 30, 1, 0))
seen = dict()
print("part 2: ", solve("AA", 26, 1, 1))