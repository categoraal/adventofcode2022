input = open('day17/input17.txt').read()
width = 7
numberOfRocks = 2022

field = [['+','1','2','3','4','5','6','7','+'],['|','.','.','.','.','.','.','.','|']]
fieldslice = ['|','.','.','.','.','.','.','.','|']

def drawScreen(X):
    screenstring = ''
    for y in range(len(X)):
        screenstring = ''
        for x in range(len(X[0])):
            screenstring += str(X[y][x])
        print(screenstring,)
    print('\n')

rocks = [[['#','#','#','#']]]
rocks.append([['.','#','.'],['#','#','#'],['.','#','.']])
rocks.append([['#','#','#'],['.','.','#'],['.','.','#']])
rocks.append([['#'],['#'],['#'],['#']])
rocks.append([['#','#'],['#','#']])

field.append(['|','.','.','.','.','.','.','.','|'])
field.append(['|','.','.','.','.','.','.','.','|'])
field.append(['|','.','.','.','.','.','.','.','|'])
field.append(['|','.','.','.','.','.','.','.','|'])
field.append(['|','.','.','.','.','.','.','.','|'])
field.append(['|','.','.','.','.','.','.','.','|'])
drawScreen(field)

def addrock(rock,instructionCounter):
    width = len(rock[0])
    height = len(rock)
    px,py = 3,len(field)-4
    canMoveDown = True
    while canMoveDown == True:
        a, px = rocklr(input[instructionCounter%len(input)],width,px,py,rock)
        instructionCounter += a
        canMoveDown,py = rockd(px,py,rock)
    drawrock(px,py,rock)
    extendfield()
    return instructionCounter

def rocklr(instruction,width,px,py,rock):
    newpos = px
    a = True
    if instruction == '<' :
        #if py < len(field):
        for y in range(len(rock)):
            for x in range(len(rock[0])):
                if rock[y][x] == '#' and field[py+y][px+x-1] != '.':
                    a = False
        if px == 1 or a == False: #check on overlapping tiles
            newpos = px
        else:
            newpos = px-1
    if instruction == '>':
        #if py < len(field):
        for y in range(len(rock)):
            for x in range(len(rock[0])):
                if rock[y][x] == '#' and field[py+y][px+x+1] != '.':
                    a = False
        if px+width-1 == 7 or a == False:
            newpos = px
        else:
            newpos = px+1
    return 1,newpos

def rockd(px,py,rock): #position x, position y, shape of the rock
    canMoveDown = True
    newpy = py-1
    #no overlap if move down
    for y in range(len(rock)):
        for x in range(len(rock[0])):
            if rock[y][x] == '#' and field[py+y-1][px+x] != '.':
                canMoveDown = False
                newpy = py
    return canMoveDown,newpy

def drawrock(px,py,rock):
    for y in range(len(rock)):
        for x in range(len(rock[0])):
            if rock[y][x] == '#':
                field[py+y][px+x] = '#'
    return 0

def extendfield():
    sum = 0
    for i in [-7,-6,-5,-4]:
        if any([i for i in field[i] if i == '#']):
            sum += 1
    for i in range(sum):
        field.append(['|','.','.','.','.','.','.','.','|'])
    return 0

instructionCounter = 0
lengths = [0]
diffs = [0]
for i in range(5000):
    a = i%5
    #print('rocknumber',a)
    instructionCounter = addrock(rocks[a],instructionCounter)
    #drawScreen(field)
    lengths.append(len(field)-8)
    diffs.append(lengths[-1] - lengths[-2])
#drawScreen(field)

file1 = open('day17/day17file.txt','w')
for i in lengths:
    file1.write(str(i))
    file1.write('\n')
    
file1.close()

def finder():
    for i in range(len(diffs)-1000):
        for j in range(i+1,len(diffs)-1000):
            if diffs[i:i+100] == diffs[j:j+100]:
                print(i,j)
                return i-j


a = finder()

step = lengths[1700+600]-lengths[600]
print(int(lengths[200]+step*(1000000000000-200)/1700))
