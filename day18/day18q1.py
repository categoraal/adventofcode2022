input = open('day18/input18.txt').read().strip().split('\n')

input = [[int(x) for x in y.split(',')] for y in input]

res = []
for x,y,z in input:
    k,l,m =(0,0,0)
    som = 6
    for j in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        u,v,w = j
        k = x+u
        l = y+v
        m = z+w
        a = [i for i in input if i==[k,l,m]]
        if any(a):
            som -= 1
    res.append(som)

print(sum(res))