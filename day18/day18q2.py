import copy
input = open('day18/input18.txt').read().strip().split('\n')
input = [[int(x) for x in y.split(',')] for y in input]

air = [[0,0,0]]
upper,lower = 22,-1
sum = 0
for i in air:
    x,y,z = i
    k,l,m =(0,0,0)
    for j in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        u,v,w = j
        k = x+u
        l = y+v
        m = z+w
        if k >= lower and k <= upper and l >= lower and l <= upper and m >= lower and m <= upper:
            if [k,l,m] not in input and [k,l,m] not in air:
                air.append([k,l,m])
            if [k,l,m] in input:
                sum += 1
print(sum)