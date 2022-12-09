import copy

input = open('day9/input9.txt').read().splitlines()
input = [row.split(' ') for row in input]

for i in range(len(input)):
    input[i][1] = int(input[i][1])

rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] #locatin tail


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
    return tail

posTail = []
for i in range(len(input)):
    for j in range(input[i][1]):
        if input[i][0] == 'U':
            rope[0][1] += 1
        if input[i][0] == 'D':
            rope[0][1] += -1
        if input[i][0] == 'L':
            rope[0][0] += -1        
        if input[i][0] == 'R':
            rope[0][0] += 1
        for k in range(len(rope)-1):
            if isTouching(rope[k],rope[k+1]) == False:
                movement(rope[k],rope[k+1])
        posTail = posTail + rope[9]

posTail = [str(i) for i in posTail]
result = ['0 0']
for i in range(int(len(posTail)/2)):
    result.append(posTail[2*i] + ' ' + posTail[2*i+1])

print(len(set(result)))