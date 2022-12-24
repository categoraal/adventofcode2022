input = open('day24/input24test.txt').read().strip().split('\n')
print(input)
sizeY,sizeX = (len(input),len(input[0]))
print(sizeY,sizeX)
board = [[y for y in x] for x in input]
[print(x) for x in board]
bu = [[x for x in y] for y in board]

def mapdir(arrow):  
    col = []
    for y in range(len(input)):
        row = []
        for x in range(len(input[0])):
            if input[y][x] == arrow:
                row.append(arrow)
            else:
                row.append('.')
        col.append(row)
    return col

br = mapdir('>')[::-1]
bl = mapdir('<')
bu = mapdir('^')
bd = mapdir('v')[::-1]

br = list(map(list,zip(*br)))
bl = list(map(list,zip(*bl)))

start = input[0].index('.')
end = input[sizeY-1].index('.')
print(start,end)

def blizzardMove():
    br.append(br.pop(0))
    bl.append(bl.pop(0))
    bu.append(bu.pop(0))
    bd.append(bd.pop(0))

queu = [[start,0]]
def round(queu):
    blizzardMove()
    res = []
    for i in queu:
        print(i)
        dir = (1,0),(-1,0),(0,1),(0,-1),(0,0)
        x,y = i
        for j in dir:
            u,v = j
            k,l = x+u,y+v
            if k > 0 and k < sizeX-2 and l > 0 and l < sizeY-2:
                if bu[l][k] == '.' and bd[sizeY-l][k]== '.' and br[k][l] == '.' and bl[k][sizeY-l]:
                    res.append([k,l])
    return res

print(round(queu))