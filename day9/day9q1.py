input = open('day9/input9.txt').read().splitlines()
input = [row.split(' ') for row in input]

for i in range(len(input)):
    input[i][1] = int(input[i][1])

head = [0,0] #location head
tail = [0,0] #locatin tail

def isTouching(head, tail):
    res = False
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        res = True
    return res

posTail = []
for i in range(len(input)):
    for j in range(input[i][1]):
        oldHead = head.copy()
        if input[i][0] == 'U':
            head[1] += 1
        if input[i][0] == 'D':
            head[1] += -1
        if input[i][0] == 'L':
            head[0] += -1        
        if input[i][0] == 'R':
            head[0] += 1
        if isTouching(head,tail) == False:
            tail = oldHead
            posTail = posTail + tail

posTail = [str(i) for i in posTail]

result = ['0 0']
for i in range(int(len(posTail)/2)):
    result.append(posTail[2*i] + ' ' + posTail[2*i+1])

print(len(set(result)))