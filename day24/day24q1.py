import sys
sys.setrecursionlimit(1000000)

input = open('day24/input24.txt').read().strip().split('\n')
#print(input)
sizeY,sizeX = (len(input),len(input[0]))
print(sizeY,sizeX)
board = [[y for y in x] for x in input]
del board[0]
del board[-1]
board = list(map(list,zip(*board)))
del board[0]
del board[-1]
board = list(map(list,zip(*board)))
#[print(x) for x in board]

def mapdir(arrow):  
    col = []
    for y in range(len(board)):
        row = []
        for x in range(len(board[0])):
            if board[y][x] == arrow:
                row.append(arrow)
            else:
                row.append('.')
        col.append(row)
    return col

br = mapdir('>')
bl = mapdir('<')
bu = mapdir('^')
bd = mapdir('v')

br = list(map(list,zip(*br))) #transpose
bl = list(map(list,zip(*bl))) #transpose

start = [input[0].index('.')-1,-1]
end = [input[sizeY-1].index('.')-1,sizeY-2]
print(start,end)

def blizzardMove():
    #br[::-1]
    br.reverse()
    br.append(br.pop(0))
    br.reverse()
    #br[::-1]
    bl.append(bl.pop(0))
    bu.append(bu.pop(0))
    bd.reverse()
    bd.append(bd.pop(0))
    bd.reverse()
    #[print(x) for x in br]
    #print('\n')
    #[print(x) for x in bl]
    #print('\n')
    #[print(x) for x in bu]
    #print('\n')
    #[print(x) for x in bd]  

queu = [start]
ronde = 0
def round(queu,ronde):
    blizzardMove()
    ronde += 1
    print('ronde',ronde,'queu',len(queu))
    res = []    
    #print(queu)
    for i in queu:
        #print(i)
        dir = (1,0),(-1,0),(0,1),(0,-1),(0,0)
        x,y = i
        for j in dir:
            u,v = j
            k,l = x+u,y+v
            if k >= 0 and k < sizeX-2 and l >= 0 and l < sizeY-2:
                if bu[l][k] == '.' and bd[l][k]== '.' and br[k][l] == '.' and bl[k][l] =='.'and [k,l] not in res:
                    res.append([k,l])
                    #print('x,y',k,l)
            if start not in res:
                res.append(start)

            if [k,l+1] == end:
                print('ronde',ronde+1)
                return 0
        
            #res.append(start)  
    
    #if ronde == 3:
    #    return 0
    #unique_data = [list(x) for x in set(tuple(x) for x in res)]
    round(res,ronde)

print(round(queu,ronde))