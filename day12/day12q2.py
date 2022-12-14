input = [[col for col in row] for row in open('day12/input12.txt').read().split('\n')]

heights = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'S':0,'E':26}
heightMap = [[heights.get(col) for col in row] for row in input]
distanceMap = [[col for col in row] for row in input]
visitedMap = [[col for col in row] for row in input]

for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] == 'S':
            start = [x,y]
            break

for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] == 'E':
            end = [x,y]
            break

stack = [[end[1],end[0]]] # type: ignore

maxdistance = len(input[0])*len(input)
for x in range(len(input[0])):
    for y in range(len(input)):
        distanceMap[y][x] = maxdistance # type: ignore
distanceMap[end[1]][end[0]] = 0 # type: ignore

for x in range(len(visitedMap[0])):
    for y in range(len(visitedMap)):
        visitedMap[y][x] = '.'
visitedMap[end[1]][end[0]] = 'x' # type: ignore

def drawScreen(X):
    screenstring = ''
    for y in range(len(X)):
        for x in range(len(X[0])):
            screenstring += str(X[y][x])
        screenstring += '\n'
    print(screenstring)

def findDistance(x,y,stack): 
    distance = distanceMap[y][x]
    height = heightMap[y][x]
    if y < len(distanceMap)-1: #down
        if distanceMap[y+1][x] > distance + 1 and (heightMap[y+1][x] - height) > -2:# type: ignore
            distanceMap[y+1][x] = distance + 1 # type: ignore
            visitedMap[y+1][x] = 'x'
            stack.append([y+1,x])
    if y > 0: #up
        if distanceMap[y-1][x] > distance + 1 and (heightMap[y-1][x] - height) > -2:# type: ignore
            distanceMap[y-1][x] = distance + 1 # type: ignore
            visitedMap[y-1][x] = 'x'
            stack.append([y-1,x])
    if x > 0: #left
        if distanceMap[y][x-1] > distance + 1 and (heightMap[y][x-1] - height) > -2:# type: ignore
            distanceMap[y][x-1] = distance + 1 # type: ignore
            visitedMap[y][x-1] = 'x'
            stack.append([y,x-1])
    if x < len(distanceMap[0])-1: #right
        if distanceMap[y][x+1] > distance + 1 and (heightMap[y][x+1] - height) > -2:# type: ignore
            distanceMap[y][x+1] = distance + 1 # type: ignore
            visitedMap[y][x+1] = 'x'
            stack.append([y,x+1])    
    return 0

step = 0
for i in stack:
    findDistance(i[1],i[0],stack) # type: ignore
    if step%10==0:
        drawScreen(visitedMap)
    step+=1
print('the minimum distance = ',min([row[0] for row in distanceMap]))
#drawScreen(visitedMap)