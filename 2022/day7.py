"""
#part 1
with open("day7input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.val = 0
        if parent != None:
            parent.children.append(self)

#go through keeping track of current directory
#when listing, if directory in current, add directory to children
#when listing, accumulate sum of all direct
root = Dir('/', None)
currentDir = root

for line in data:
    line = line.split()
    if line[0] == "$":
        #command
        if line[1] == "cd":
            if line[2] == "/":
                currentDir = root
            elif line[2] == "..":
                currentDir = currentDir.parent
            else:
                for c in currentDir.children:
                    if c.name == line[2]:
                        currentDir = c
                        break
    elif line[0] == "dir":
        #add directory to current
        name = line[1]
        new = Dir(name, currentDir)
    else:
        size = int(line[0])
        currentDir.val += size

def search(node, total):
    indirect = 0
    for c in node.children:
        res, total = search(c, total)
        indirect += res
    node.val += indirect

    if node.val <= 100000:
        total += node.val

    return node.val, total

print(list(search(root, 0))[1])"""

#part 2

with open("day7input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0], f.readlines()))

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.val = 0
        if parent != None:
            parent.children.append(self)

#go through keeping track of current directory
#when listing, if directory in current, add directory to children
#when listing, accumulate sum of all direct
root = Dir('/', None)
currentDir = root

for line in data:
    line = line.split()
    if line[0] == "$":
        #command
        if line[1] == "cd":
            if line[2] == "/":
                currentDir = root
            elif line[2] == "..":
                currentDir = currentDir.parent
            else:
                for c in currentDir.children:
                    if c.name == line[2]:
                        currentDir = c
                        break
    elif line[0] == "dir":
        #add directory to current
        name = line[1]
        new = Dir(name, currentDir)
    else:
        size = int(line[0])
        currentDir.val += size

def search(node, total):
    indirect = 0
    for c in node.children:
        res, total = search(c, total)
        indirect += res
    node.val += indirect

    if node.val <= 100000:
        total += node.val

    return node.val, total


def search2(node, target, minSize):
    if node.val >= target and node.val < minSize:
        minSize = node.val
    for c in node.children:
        minSize = search2(c, target, minSize)

    return minSize



totalSpace = list(search(root, 0))[0]
unused = 70000000-totalSpace
toDelete = 30000000 - unused
print(search2(root, toDelete, totalSpace))