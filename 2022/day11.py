"""
#part 1
from collections import deque
with open("2022/day11input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0].strip(), f.readlines()))

class Monkey:
    def __init__(self):
        self.items = deque()
        self.multiply = False
        self.changer = None
        self.divisor = 0
        self.trueDest = 0
        self.falseDest = 0
        self.inspected = 0

    def inspect(self, monkeys):
        self.inspected += len(self.items)
        while self.items:
            current = self.items.popleft()
            toChange = self.changer
            if toChange == None:
                toChange = current
            if self.multiply:
                current *= toChange
            else:
                current += toChange
            #current //= 3
            if current%self.divisor == 0:
                monkeys[self.trueDest].items.append(current)
            else:
                monkeys[self.falseDest].items.append(current)

monkeys = []

index = 0
while index < len(data):
    monkeys.append(Monkey())
    index += 1
    toAdd = list(map( lambda x: int(x.replace(",", "")), data[index].split()[2:]))
    monkeys[-1].items.extend(toAdd)
    index += 1
    if data[index].split()[-2] == "*":
        monkeys[-1].multiply = True
    if data[index].split()[-1] != "old":
        monkeys[-1].changer = int(data[index].split()[-1])
    index += 1
    monkeys[-1].divisor = int(data[index].split()[-1])
    index += 1
    monkeys[-1].trueDest = int(data[index].split()[-1])
    index += 1
    monkeys[-1].falseDest = int(data[index].split()[-1])
    index += 2

for _ in range(0, 2):
    for m in monkeys:
        m.inspect(monkeys)

for m in monkeys:
    m.inspect(monkeys)

max1 = 0
max2 = 0
for m in monkeys:
    if m.inspected > max1:
        max2 = max1
        max1 = m.inspected
    elif m.inspected > max2:
        max2 = m.inspected

print(max1*max2)
"""


#part 2

from collections import deque
with open("2022/day11input.txt", "r") as f:
    data = list(map(lambda x:x.split("\n")[0].strip(), f.readlines()))

class Monkey:
    def __init__(self):
        self.items = deque()
        self.multiply = False
        self.changer = None
        self.divisor = 0
        self.trueDest = 0
        self.falseDest = 0
        self.inspected = 0

    def convert(self, divisors):
        new = deque()
        while self.items:
            temp = self.items.popleft()
            empty = []
            for d in divisors:
                empty.append(temp%d)
            new.append(empty)
        self.items = new

    def inspect(self, monkeys, divisors):
        self.inspected += len(self.items)
        while self.items:
            remainders = self.items.popleft()
            new = []
            if self.multiply:
                if self.changer == None:
                    for i in range(0, len(remainders)):
                        new.append((remainders[i] * remainders[i])%divisors[i])
                else:
                    for i in range(0, len(remainders)):
                        new.append((remainders[i] * self.changer)%divisors[i])
            else:
                for i in range(0, len(remainders)):
                    new.append((remainders[i] + self.changer)%divisors[i])

            ind = divisors.index(self.divisor)
            if new[ind] == 0:
                monkeys[self.trueDest].items.append(new)
            else:
                monkeys[self.falseDest].items.append(new)

monkeys = []
divisors = []
index = 0
while index < len(data):
    monkeys.append(Monkey())
    index += 1
    toAdd = list(map( lambda x: int(x.replace(",", "")), data[index].split()[2:]))
    monkeys[-1].items.extend(toAdd)
    index += 1
    if data[index].split()[-2] == "*":
        monkeys[-1].multiply = True
    if data[index].split()[-1] != "old":
        monkeys[-1].changer = int(data[index].split()[-1])
    index += 1
    monkeys[-1].divisor = int(data[index].split()[-1])
    divisors.append(monkeys[-1].divisor)
    index += 1
    monkeys[-1].trueDest = int(data[index].split()[-1])
    index += 1
    monkeys[-1].falseDest = int(data[index].split()[-1])
    index += 2

for m in monkeys:
    m.convert(divisors)

for _ in range(0, 10000):
    for m in monkeys:
        m.inspect(monkeys, divisors)

max1 = 0
max2 = 0
for m in monkeys:
    if m.inspected > max1:
        max2 = max1
        max1 = m.inspected
    elif m.inspected > max2:
        max2 = m.inspected

print(max1*max2)