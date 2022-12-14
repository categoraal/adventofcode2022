#x-->
#y (input = (x,y))
#|
#v
input = open('day14/input14.txt').read().strip().split('\n')
input = [[[int(x) for x in col.split(',')] for col in row.split(' -> ')] for row in input]
sandsource = [500,0]

#find the boundaries of the cave map
maxY = max(map(max,[[col[1] for col in row] for row in input]))+2
maxX = 500 + maxY#(max(max(map(max, input)))) #upper x boundary
minX = 500 - maxY#(min(map(min, [[col[0] for col in row] for row in input])))
print(maxY)
#generate a kaart
kaart = [list(range(minX,maxX+1,1)) for i in range(maxY+1)]
def generateRock(x):
    dy = x[1][1]-x[0][1]
    dx = x[1][0]-x[0][0]
    if dx > 0:
        for i in range(dx+1):
            kaart[x[0][1]][x[0][0]+i-minX] = '#' # type: ignore
    if dx < 0:
        for i in range(abs(dx)+1):
            kaart[x[0][1]][x[0][0]-i-minX] = '#' # type: ignore       
    if dy > 0:
        for i in range(dy+1):
            kaart[x[0][1]+i][x[0][0]-minX] = '#' # type: ignore
    if dy < 0:
        for i in range(abs(dy)+1):
            kaart[x[0][1]-i][x[1][0]-minX] = '#' # type: ignore

def generateMap(input):
    for x in range(len(kaart[0])):
        for y in range(len(kaart)):
            kaart[y][x] = '.'# type: ignore    
    for i in range(len(input)):
        for j in range(len(input[i])-1):
            #print(input[i][j:j+2])
            generateRock(input[i][j:j+2])

def drawScreen(X):
    screenstring = ''
    for y in range(len(X)):
        for x in range(len(X[0])):
            screenstring += str(X[y][x])
        screenstring += '\n'
    print(screenstring)

generateMap(input)
kaart[0][500-minX] = 'S' # type: ignore
for i in range(len(kaart[0])):
    kaart[maxY][i] = '#'  # type: ignore
drawScreen(kaart)

def dropSand(x,y):
    if kaart[0][500-minX] == 'o':
        return 0
    res = 0
    try:
        #print('test')
        if kaart[y+1][x] =='.':
            res = dropSand(x,y+1)
        elif kaart[y+1][x-1] =='.':
            res = dropSand(x-1,y+1)
        elif kaart[y+1][x+1] =='.':
            res = dropSand(x+1,y+1)
        else:
            kaart[y][x] ='o' # type: ignore
            res = 1
        
    except:
        res = 0
    return res
        
oldSandCounter = -1
sandCounter = 0
res = 0
while sandCounter > oldSandCounter:
#for i in range(26):
    oldSandCounter = sandCounter
    sandCounter += dropSand(500-minX,0)
    #print(sandCounter)
    #result = [[x for x in y if x == 'o'] for y in kaart]
    #sandCounter = (sum(map(len, result)))
        
    

#print(sandCounter)
drawScreen(kaart)
print(sandCounter)
#drawScreen(kaart)