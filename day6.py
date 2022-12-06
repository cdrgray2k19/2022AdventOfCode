"""
#part 1
with open("day6input.txt", "r") as f:
    data = list(map(lambda x: x.strip("\n"), f.readlines()))[0]

store = []
for i in range(0, len(data)-4):
    if len(store) < 4:
        store.append(data[i])
    else:
        store.pop(0)
        store.append(data[i])
    if len(set(store)) == 4:
        print(i+1)
        break"""


#part 2
with open("day6input.txt", "r") as f:
    data = list(map(lambda x: x.strip("\n"), f.readlines()))[0]

store = []
for i in range(0, len(data)-14):
    if len(store) < 14:
        store.append(data[i])
    else:
        store.pop(0)
        store.append(data[i])
    if len(set(store)) == 14:
        print(i+1)
        break