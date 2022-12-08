input = open('day8/input8.txt').read().split('\n')
forest = [[int(col) for col in row] for row in input]

def scenicScore(x,y,forest):
    score = 0
    heightTree = forest[y][x]
    horizontal = forest[y]
    vertical = [row[x] for row in forest]
    horizontalLeft = list(reversed(horizontal[:x]))
    horizontalRight = (horizontal[x+1:])
    verticalLeft = list(reversed(vertical[:y]))
    verticalRight = (vertical[y+1:])
    a = viewingDistance(heightTree,horizontalLeft)
    b = viewingDistance(heightTree,horizontalRight)
    c = viewingDistance(heightTree,verticalLeft)
    d = viewingDistance(heightTree,verticalRight)
    return a*b*c*d

def viewingDistance(height, row):
    distance = 0
    for i in range(len(row)):
        if row[i] > height:
            break
        elif row[i] == height:
            distance += 1
            break
        else:
            distance += 1
    return distance

heighestScore = 0
for i in range(len(forest)-2):
    for j in range(len(forest)-2):
        sc = scenicScore(i+1,j+1,forest)
        if sc > heighestScore:
            heighestScore = sc

print('The heigherst scenic score = ',heighestScore)