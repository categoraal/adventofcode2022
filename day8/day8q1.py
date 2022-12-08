input = open('day8/input8.txt').read().split('\n')
forest = [[int(col) for col in row] for row in input]
    
def visibletree(x,y,forest):
    res = False
    heightTree = forest[y][x]
    horizontal = forest[y]
    vertical = [row[x] for row in forest]
    horizontalLeft = max(horizontal[:x])
    horizontalRight = max(horizontal[x+1:])
    verticalLeft = max(vertical[:y])
    verticalRight = max(vertical[y+1:])
    if heightTree > horizontalLeft or heightTree > horizontalRight or heightTree > verticalLeft or heightTree > verticalRight:
        res = True
    return res

sum = 4*98
print(visibletree(1,1,forest))
print(visibletree(1,2,forest))
for i in range(len(forest)-2):
    for j in range(len(forest)-2):
        if visibletree(i+1,j+1, forest) == True:
            sum += 1

print('Het aantal zichtbare bomen =', sum)

