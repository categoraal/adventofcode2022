input = open('day4/input4.txt').read().split('\n')
print(type(input[0]))

def parse(x):
    z = x.split(',')
    y = z[0].split('-'), z[1].split('-')
    res = [int(y[0][0]),int(y[0][1]),int(y[1][0]),int(y[1][1])]
    return res

z = parse(input[0])
sum = 0
for i in range(len(input)):
    x = parse(input[i])
    if (x[0] <= x[2] and x[1] >= x[3]) or (x[0] >= x[2] and x[1] <= x[3]):
        sum += 1
print(sum)