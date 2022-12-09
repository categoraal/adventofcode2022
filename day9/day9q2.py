import copy

input = open('day9/input9.txt').read().splitlines()
input = [row.split(' ') for row in input]

for i in range(len(input)):
    input[i][1] = int(input[i][1])

rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] #locatin tail
#print('first rope:',rope)

def isTouching(head, tail):
    res = False
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        res = True
    return res

def movement(head, tail):
    right = 0
    up = 0
    ud = head[1] - tail[1]
    rl = head[0] - tail[0]
    if ud > 0:
        up = 1
    if ud < 0:
        up = -1
    if rl > 0:
        right = 1
    if rl < 0:
        right = -1
    tail[0] += right
    tail[1] += up
    print(rl, ud)
    return tail

posTail = []
for i in range(len(input)):
    oldrope = copy.deepcopy(rope)
    print('rope befor instruction',rope)
    print(input[i])
    for j in range(input[i][1]):
        if input[i][0] == 'U':
            rope[0][1] += 1
        if input[i][0] == 'D':
            rope[0][1] += -1
        if input[i][0] == 'L':
            rope[0][0] += -1        
        if input[i][0] == 'R':
            rope[0][0] += 1
#        print('head has moved, tail has not',rope)
#        print(oldrope)
        for k in range(len(rope)-1):
 #           print(k)
            if isTouching(rope[k],rope[k+1]) == False:
                movement(rope[k],rope[k+1])
#                print('head',rope[k],'tail',rope[k+1])
#                rope[k+1] = oldrope[k]
#                print('new',rope[k+1],'from oldrope',oldrope[k])
#                print('rope',rope)
#                print('oldrope',oldrope)
#                print(rope)
    #print(rope)
        posTail = posTail + rope[9]
print(rope)
posTail = [str(i) for i in posTail]
print(posTail)
result = ['0 0']
for i in range(int(len(posTail)/2)):
    result.append(posTail[2*i] + ' ' + posTail[2*i+1])

print(len(set(result)))