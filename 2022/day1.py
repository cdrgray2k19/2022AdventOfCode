"""
#part 1
f = open("day1input.txt", 'r')
sum = 0
max = 0
for line in f.readlines():
    if line == "\n":
        if sum > max:
            max = sum
        sum = 0
    else:
        line = line.replace("\n", "")
        sum += int(line)

print(max)"""
#part 2
f = open("day1input.txt", 'r')
sum = 0
max1 = 0
max2 = 0
max3 = 0
for line in f.readlines():
    if line == "\n":
        if sum > max1:
            max3 = max2
            max2 = max1
            max1 = sum
        elif sum > max2:
            max3 = max2
            max2 = sum
        elif sum > max3:
            max3 = sum
        sum = 0
    else:
        line = line.replace("\n", "")
        sum += int(line)

print(max1+max2+max3)