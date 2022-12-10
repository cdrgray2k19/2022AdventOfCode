"""
#part 1
with open("day3input.txt", "r") as f:
    data = list(map(lambda x: x.replace("\n", "") , f.readlines()))


total = 0
for packs in data:
    pack1 = packs[0:len(packs)//2]
    pack2 = packs[len(packs)//2:]
    seen = set()
    for c in pack1:
        seen.add(c)
    for c in pack2:
        if c in seen:
            if ord(c) > 91:
                #lowercase
                priority = ord(c) - ord('a') + 1
                break
            else:
                priority = ord(c) - ord('A') + 27
                break
    total += priority

print(total)"""

#part 2

with open("day3input.txt", "r") as f:
    data = list(map(lambda x: x.replace("\n", "") , f.readlines()))


total = 0
for i in range(2, len(data), 3):
    pack1 = data[i]
    pack2 = data[i-1]
    pack3 = data[i-2]

    seen1 = set()
    seen2 = set()
    for c in pack1:
        seen1.add(c)
    for c in pack2:
        if c in seen1:
            seen2.add(c)
    for c in pack3:
        if c in seen2:
            if ord(c) > 91:
                #lowercase
                priority = ord(c) - ord('a') + 1
                break
            else:
                priority = ord(c) - ord('A') + 27
                break
    total += priority
print(total)