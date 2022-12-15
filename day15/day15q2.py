import re
input = open('day15/input15.txt').read().strip().split('\n')
input = [[int(j) for j in re.findall(r'[\-]\d+|\d+',i)] for i in input]
rowToCheck = 4000000

for i in input:
    i.append(abs(i[0]-i[2]) + abs(i[1]-i[3]))

def checkpoint(x,y):
    for i in input:
        distance = abs(x-i[0])+abs(y-i[1])
        if distance <= i[4]:
            return 0
    print('the frequency =',x*4000000+y)
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
                    return 1
            cx += i[0]
            cy += i[1]
    return 0

for i in input:
    res = checkboundary(i)
    if res == 1:
        break