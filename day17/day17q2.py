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
for i in range(500000):
    a = i%5
    #print('rocknumber',a)
    instructionCounter = addrock(rocks[a],instructionCounter)
    #drawScreen(field)
    lengths.append(len(field)-8)
    diffs.append(lengths[-1] - lengths[-2])
#drawScreen(field)
print(diffs[:100])
print(len(diffs))
print(len(input))
print(len(field)-8)
print(lengths[10091])
print(lengths[10091*2])


def guess_seq_len(seq,offset):
    guess = 1
    max_len = int(len(seq) / 2)
    for x in range(2, max_len):
        if seq[offset+0:offset+x] == seq[offset+x:offset+2*x] :
            return x

#for offset in range(1000):
#    res = guess_seq_len(lengths,offset)
#    if res != None:
#        print(res)

#for i in range(20000):
#    if lengths[i-10000+10091*10] - lengths[i-5000+10091*5] == lengths[i-5000+10091*5]:
#        print('i',i)

#print(lengths[10091*5])
#print(lengths[10091*5*2])
#print(lengths[10091*5*3])
#print(lengths[10091*5*4])

file1 = open('day17/day17file.txt','w')
for i in lengths:
    file1.write(str(i))
    file1.write('\n')
    
file1.close()