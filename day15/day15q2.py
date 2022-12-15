#X left <--- ----> right
#Y ^ up -y
#  v down +y

import re
input = open('day15/input15test.txt').read().strip().split('\n')
input = [[int(j) for j in re.findall(r'[\-]\d+|\d+',i)] for i in input]
rowToCheck = 20

#print(input)

inputT = list(zip(*input))
xmax, xmin = max(max(inputT[0]),max(inputT[2])),min(min(inputT[0]),min(inputT[2]))
ymax, ymin = max(max(inputT[1]),max(inputT[3])),min(min(inputT[1]),min(inputT[3]))
#print(xmin,xmax,ymin,ymax)

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
print(xmin,xmax,ymin,ymax)
print(xmax-xmin,ymax-ymin)


rowy = []
for i in range(xmax-xmin):
    rowy += '.'
#print(rowy)
rowx = rowy.copy()
row = []
for i in input:
    #print(i)
    distance = abs(i[0]-i[2]) + abs(i[1]-i[3])
    #print('distance between beacons',distance)
    up = i[1] - distance
    right = i[0] + distance
    down = i[1] + distance
    left = i[0] - distance
    diff = abs(i[1] - rowToCheck)
    #print('distance to row from beacon',diff)
    if diff <= distance:
        xmov = distance-diff
        row.append(i[0]-xmin-xmov)
        row.append(i[0]-xmin+xmov+1)
        
        
        
        for j in range(2*xmov+1):
        #    #print(j)
            rowy[i[0]-xmin-xmov+j] = '#'
        #    #print(i[0]-xmin-xmov+j)

print(row)

for i in range(int(len(row)/2)):
    #print('diff',row[i*2]-row[i*2+1])
    for j in range(row[i*2+1]-row[i*2]):
        #print(j+row[i*2],j)
        rowx[j+row[i*2]] = '#'


for i in input:
    #if i[1] == rowToCheck:
    #    rowy[i[0]-xmin] = 'S'
    if i[3] == rowToCheck:
        rowy[i[2]-xmin] = 'B'
        rowx[i[2]-xmin] = 'B'

#print(rowy)

#print(rowx)
sum = 0
for i in rowx:
    if i == '#':
        sum += 1
print(len(rowy))

print(sum)