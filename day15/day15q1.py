import re
input = open('day15/input15.txt').read().strip().split('\n')
input = [[int(j) for j in re.findall(r'[\-]\d+|\d+',i)] for i in input]
rowToCheck = 2000000

inputT = list(zip(*input))
xmax, xmin = max(max(inputT[0]),max(inputT[2])),min(min(inputT[0]),min(inputT[2]))
ymax, ymin = max(max(inputT[1]),max(inputT[3])),min(min(inputT[1]),min(inputT[3]))

for i in input:
    distance = abs(i[0]-i[2]) + abs(i[1]-i[3])
    up = i[1] - distance
    right = i[0] + distance
    down = i[1] + distance
    left = i[0] - distance
    if down > ymax:
        ymax = up
    if up < ymin:
        ymin = up
    if right > xmax:
        xmax = right
    if left < xmin:
        xmin = left

rowy = []
for i in range(xmax-xmin):
    rowy += '.'

for i in input:
    distance = abs(i[0]-i[2]) + abs(i[1]-i[3])
    up = i[1] - distance
    right = i[0] + distance
    down = i[1] + distance
    left = i[0] - distance
    diff = abs(i[1] - rowToCheck)
    if diff <= distance:
        xmov = distance-diff
        for j in range(2*xmov+1):
            rowy[i[0]-xmin-xmov+j] = '#'

for i in input:
    if i[3] == rowToCheck:
        rowy[i[2]-xmin] = 'B'

sum = 0
for i in rowy:
    if i == '#':
        sum += 1
print('awnser day 15 question 1 = ',sum)