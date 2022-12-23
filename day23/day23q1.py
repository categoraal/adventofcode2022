#north is up
#north, south, west, east (order) then south,west,east,norht and so on

input = open('day23/input23.txt').read().strip().split('\n')
elfloc = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == '#':
            elfloc.append([x,y])

#print(len(elfloc))
#print(len(elfloc))
def common(a,b): 
    c = [value for value in a if value in b]
    #print('border',c)
    return any(c)

def newloc(round):
    #print('round',round)
    direction = (0,-1),(0,1),(-1,0),(1,0)
    newlocations = []

    for i in range(len(elfloc)):
        #print(i)
        #print('elfloc',elfloc[i])
        newlocations.append(elfloc[i])
        x,y = elfloc[i]
        border = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1]]
        south = [[x-1,y+1],[x,y+1],[x+1,y+1]]
        north = [[x-1,y-1],[x,y-1],[x+1,y-1]]
        west = [[x-1,y-1],[x-1,y],[x-1,y+1]]
        east = [[x+1,y-1],[x+1,y],[x+1,y+1]]
        directioncheck = [north,south,west,east]
        if common(elfloc,border) == True:
            for j in range(len(direction)):
                a,b,c = directioncheck[(round+j)%4]
                #print('abc',a,b,c)
                if a not in elfloc and b not in elfloc and c not in elfloc:
                    newlocations[i] = [x+direction[(round+j)%4][0],y+direction[(round+j)%4][1]]
                    break
    #print(elfloc)
    if elfloc == newlocations:
        print('round',round+1)
        return 1

    ans = [r for r in newlocations if newlocations.count(r) > 1]        
    for i in range(len(elfloc)):
        #print('test')
        if newlocations[i] not in ans:
            elfloc[i] = newlocations[i]

    return 0
#print(elfloc)
for i in range(10000):
    #print(i)
    if newloc(i) == 1:
        break

    if i == 9:
        X = [x[0] for x in elfloc]
        Y = [x[1] for x in elfloc]
        print((min(X)-(max(X)+1))*(min(Y)-(max(Y)+1))-len(elfloc))