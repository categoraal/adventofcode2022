#start leftmost open tile   -x <--- ----> x   y v & ^ -y
#stop at wall
import re
input = open('day22/input22.txt').read()
board,moves = input.split('\n\n')
board = board.split('\n')
distances = [int(x) for x in re.findall(r'\d+',moves)]
directions = re.findall(r'\D',moves)

startx = (board[0].index('.'))
starty = 0
direction = (1,0),(0,1),(-1,0),(0,-1) #x,y #right, down, left, up


bsX = int(len(board[0])/3)
bsY = int(len(board)/4)

b1 = [x[bsX:2*bsX] for x in board[:bsY]]
b2 = [x[2*bsX:3*bsX] for x in board[:bsY]]
b3 = [x[bsX:2*bsX] for x in board[bsY:2*bsY]]
b4 = [x[:bsX] for x in board[2*bsY:3*bsY]]
b5 = [x[bsX:2*bsX] for x in board[2*bsY:3*bsY]]
b6 = [x[:bsX] for x in board[3*bsY:4*bsY]]
#[print(x) for x in b3]

#    b1 b2
#    b3
# b4 b5
# b6

def move(loc,cb,facing,dis,x):
    nx,ny = loc
    a = facing[0]
    b = facing[1]
    for i in range(dis):
        if nx+a < 0 or nx+a > 49 or ny+b < 0 or ny+b > 49:
            cb,[nx,ny] = wrap(cb,loc,facing)
        elif cb[ny+b][nx+a] == '#':
            break
        else:
            nx += a
            ny += b
            loc = [nx,ny]
    return [nx,ny],cb

def wrap(board, loc, facing):
    newboard = board
    newpos = loc
    x,y = loc
    if board == b1: #done
        match facing:
            case (1,0): #right
                if b2[y][0] == '.':
                    newboard = b2
                    newpos = [0,y]
            case (0,1): #down
                if b3[0][x] == '.':
                    newboard = b3
                    newpos = [x,0]
            case (-1,0): #left
                if b2[y][49] == '.':
                    newboard = b2
                    newpos = [49,y]
            case (0,-1): #up
                if b5[49][x] == '.':
                    newboard = b5
                    newpos = [x,49]
    if board == b2: #done
        match facing:
            case (1,0): #right
                if b1[y][0] == '.':
                    newboard = b1
                    newpos = [0,y]
            case (0,1): #down
                if b2[0][x] == '.':
                    newboard = b2
                    newpos = [x,0]
            case (-1,0): #left
                if b1[y][49] == '.':
                    newboard = b1
                    newpos = [49,y]
            case (0,-1): #up
                if b2[49][x] == '.':
                    newboard = b2
                    newpos = [x,49]
    if board == b3: #done
        match facing:
            case (1,0): #right
                if b3[y][0] == '.':
                    newboard = b3
                    newpos = [0,y]
            case (0,1): #down
                if b5[0][x] == '.':
                    newboard = b5
                    newpos = [x,0]
            case (-1,0): #left
                if b3[y][49] == '.':
                    newboard = b3
                    newpos = [49,y]
            case (0,-1): #up
                if b1[49][x] == '.':
                    newboard = b1
                    newpos = [x,49]
    if board == b4: #done
        match facing:
            case (1,0): #right
                if b5[y][0] == '.':
                    newboard = b5
                    newpos = [0,y]
            case (0,1): #down
                if b6[0][x] == '.':
                    newboard = b6
                    newpos = [x,0]
            case (-1,0): #left
                if b5[y][49] == '.':
                    newboard = b5
                    newpos = [49,y]
            case (0,-1): #up
                if b6[49][x] == '.':
                    newboard = b6
                    newpos = [x,49]
    if board == b5: #done
        match facing:
            case (1,0): #right
                if b4[y][0] == '.':
                    newboard = b4
                    newpos = [0,y]
            case (0,1): #down
                if b1[0][x] == '.':
                    newboard = b1
                    newpos = [x,0]
            case (-1,0): #left
                if b4[y][49] == '.':
                    newboard = b4
                    newpos = [49,y]
            case (0,-1): #up
                if b3[49][x] == '.':
                    newboard = b3
                    newpos = [x,49]
    if board == b6: #done
        match facing:
            case (1,0): #right
                if b6[y][0] == '.':
                    newboard = b6
                    newpos = [0,y]
            case (0,1): #down
                if b4[0][x] == '.':
                    newboard = b4
                    newpos = [x,0]
            case (-1,0): #left
                if b6[y][49] == '.':
                    newboard = b6
                    newpos = [49,y]
            case (0,-1): #up
                if b4[49][x] == '.':
                    newboard = b4
                    newpos = [x,49]
    return newboard, newpos

def coc(cb, loc):
    col,row = loc
    if cb == b1:
        return  col+50,row
    if cb == b2:
        return col + 100,row
    if cb == b3:
        return  col+50,row + 50
    if cb == b4:
        return  col,row  + 100
    if cb == b5:
        return  col+50,row+100
    if cb == b6:
        return col,row + 150

loc,cb = move([0,0],b1,(1,0),distances[0],0)
directionindex = 0

for i in range(len(directions)):
    if directions[i] == 'R':
        directionindex = (directionindex+1)%4
    else:
        directionindex = (directionindex-1)%4
    facing = direction[directionindex]
    dis = distances[i+1]
    loc, cb = move(loc,cb,facing,dis,i)
            #print(facing,dis)

col,row = loc
match facing: #type: ignore
    case (1,0):
        scoreDir = 0
    case (0,1):
        scoreDir = 1
    case (-1,0):
        scoreDir = 2
    case (0,-1):
        scoreDir = 3

if cb == b1:
    print('b1 password = ', 1000 * (row + 1) + 4*(col + 50 + 1) + scoreDir) #type: ignore
if cb == b2:
    print('b2 password = ', 1000 * (row + 1) + 4*(col + 100 + +1) + scoreDir) #type: ignore
if cb == b3:
    print('b3 password = ', 1000 * (row + 50 + 1) + 4*(col+50 +1) + scoreDir) #type: ignore
if cb == b4:
    print('b4 password = ', 1000 * (row  + 100 + 1) + 4*(col +1) + scoreDir) #type: ignore
if cb == b5:
    print('b5 password = ', 1000 * (row + 100 + 1) + 4*(col+50 +1) + scoreDir) #type: ignore
if cb == b6:
    print('b6 password = ', 1000 * (row + 150 + 1) + 4*(col + 1) + scoreDir) #type: ignore
