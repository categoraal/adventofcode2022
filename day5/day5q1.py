input = open('day5/input5.txt').read()
stacks, moves = input.split('\n\n')
stacks = stacks.split('\n')

rows =[]
columns =[]
for j in range(9):
    columns = []
    for i in range(len(stacks)-1):
        if stacks[i][1+4*j] != ' ':
            columns += stacks[i][1+4*j]
    rows.append(columns)

moves = moves.replace('move ','').replace('from ','').replace('to ','').replace('\n',' ').split(' ')
moves = [eval(i) for i in moves]

for i in range(len(rows)):
    rows[i] = list(reversed(rows[i]))

for i in range(int(len(moves)/3)):
    crates = moves[3*i]
    a = int(moves[3*i+1])-1
    b = int(moves[3*i+2])-1
    for j in range(int(crates)):
        z = rows[a].pop()
        rows[b].append(z)

res = []
for i in range(9):
    res += rows[i].pop()
res = ''.join(res)
print(res)