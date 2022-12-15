#X left <--- ----> right
#Y ^ up -y
#  v down +y

import re
input = open('day15/input15.txt').read().strip().split('\n')
input = [[int(j) for j in re.findall(r'[\-]\d+|\d+',i)] for i in input]
rowToCheck = 4000000

#print(input)

inputT = list(zip(*input))
xmax, xmin = max(max(inputT[0]),max(inputT[2])),min(min(inputT[0]),min(inputT[2]))
ymax, ymin = max(max(inputT[1]),max(inputT[3])),min(min(inputT[1]),min(inputT[3]))
#print(xmin,xmax,ymin,ymax)
for i in input:
    i.append(abs(i[0]-i[2]) + abs(i[1]-i[3]))
[print(i) for i in input]

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

def checkpoint(x,y):
    for i in input:
        distance = abs(x-i[0])+abs(y-i[1])
        if distance <= i[4]:
            return 0
    return 1

def checkboundary(x):
    res = 0
    #traverse the border:
    sx, sy, bx, by, d = x
    dist = abs(sx-bx) + abs(sy-by)
    cx,cy = sx,sy-d-1
    for i in [[1,1],[-1,1],[-1,-1],[1,-1]]:
        for j in range(d+1):
            if cx <= rowToCheck and cx >= 0 and cy >= 0 and cy <= rowToCheck: #in boundary, check xy-s_k < d-s_k
                res = checkpoint(cx, cy)
                if res == 1:
                    print('coords',cx,cy)
                    print(cx*4000000+cy)
                    return 1
            cx += i[0]
            cy += i[1]
    #print('s',sx, sy,'b',bx,by,'dist', dist)

    return 0



for i in input:
    res = checkboundary(i)
    if res == '1':
        break