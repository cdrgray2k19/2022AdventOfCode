with open("day13input.txt", "r") as f:
    data = list(map(lambda x:x.replace("\n", ""), f.read().split("\n")))

def getNextValInd(arr, start):
    for i in range(start+1, len(arr)):
        if arr[i] == ",":
            continue
        return i


def compare(left, right, startL, startR):
    leftInd = startL
    rightInd = startR
    while True:
        leftInd = getNextValInd(left, leftInd)
        rightInd = getNextValInd(right, rightInd)

        if left[leftInd] == "]" and right[rightInd] == "]":
            return None, leftInd, rightInd
        elif left[leftInd] == "]":
            return True, leftInd, rightInd
        elif right[rightInd] == "]":
            return False, leftInd, rightInd
    
        if left[leftInd] == "[" and right[rightInd] == "[":
            res, leftInd, rightInd = compare(left, right, leftInd, rightInd)
            if res != None:
                return res, leftInd, rightInd 
        elif left[leftInd] == "[":
            right.insert(rightInd, "[")
            right.insert(rightInd+2, "]")
        elif right[rightInd] == "[":
            left.insert(leftInd, "[")
            left.insert(leftInd+2, "]")
        else:
            if int(left[leftInd]) < int(right[rightInd]):
                return True, leftInd, rightInd
            elif int(left[leftInd]) > int(right[rightInd]):
                return False, leftInd, rightInd

def convert(s):
    res = []
    store = ""
    for i in range(0, len(s)):
        if s[i] in [",", "]", "["]:
            if store != "":
                res.append(store)
                store = ""
            res.append(s[i])
        else:
            store += s[i]
    return res
            

total = 0
pair = 1
packets = []
for i in range(0, len(data),3):
    top = data[i]
    left = convert(top)
    bottom = data[i+1]
    right = convert(bottom)
    res, leftInd, rightInd = compare(left, right, 0, 0)
    packets.append(top)
    packets.append(bottom)
    if res:
        total += pair
    pair += 1

taken = [False] * len(packets)
print(int(total))
packets.append("[[2]]")
packets.append("[[6]]")
order = []
while packets:
    add = packets.pop()
    if len(order) == 0:
        order.append(add)
        continue
    added = False
    for i in range(0, len(order)):
        res, void1, void2 = compare(convert(order[i]), convert(add), 0, 0)
        if not res:
            order.insert(i, add)
            added = True
            break
    
    if not added:
        order.append(add)

total2 = 1
for i in range(0, len(order)):
    if order[i] in ["[[2]]", "[[6]]"]:
        total2 *= i+1

print(total2)