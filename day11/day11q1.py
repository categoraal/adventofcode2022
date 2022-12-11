import math

input = open('day11/input11.txt').read()
input = input.split('\n\n')
input = [x.split('\n') for x in input]

def startingItems(x):
    items = []
    x = x[18:].split(', ')
    for i in x:
        if i.isdigit():
            items.append(int(i))
    return items

def doFunc(x, oldValue): #runs the first function and divides by 3
    new = 0
    x = x[23:].split()
    if x[0] == '*' and x[1] != 'old':
        new = oldValue * int(x[1])
    if x[0] == '*' and x[1] == 'old':
        new = oldValue * oldValue
    if x[0] == '+' and x[1].isdigit:
        new = oldValue + int(x[1])
    if x[0] == '+' and x[1] == 'old':
        new = oldValue + oldValue
    return math.floor(new/3)
    
def throw(x, worry): #tells me to witch monkey the item is thrown
    monkey = 0
    test = int(x[3].split(' ')[-1])
    monkey1 = int(x[4].split(' ')[-1])
    monkey2 = int(x[5].split(' ')[-1])
    if worry%test == 0:
        monkey = monkey1
    else:
        monkey = monkey2
    return monkey

items = []
for i in input:
    items.append(startingItems(i[1]))

inspections = [0,0,0,0,0,0,0,0]
def round(input, items, inspections):
    for i in range(len(input)): #first monkey first
        length = len(items[i])
        for j in range(length):
            inspections[i] += 1
            if length == 0:
                break
            items[i] = list(reversed(items[i]))
            worry = doFunc(input[i][2],items[i][-1])
            monkey = throw(input[i], worry)
            items[i].pop()
            items[monkey].append(worry)
            items[i] = list(reversed(items[i]))
    return inspections

for i in range(20):
    inspections = round(input, items, inspections)

inspections = sorted(inspections)
print(inspections[-1]*inspections[-2])