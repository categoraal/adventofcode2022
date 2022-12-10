input = open('day10/input10.txt').read().split('\n')
input = [row.split(' ') for row in input]

def valueX(input):
    instruction = [1]
    for i in range(len(input)):
        if input[i][0] == 'noop':
            instruction.append(instruction[-1]) 
        if input[i][0] != 'noop':
            instruction.append(instruction[-1]) 
            instruction.append(instruction[-1] + int(input[i][1]))
    return instruction

X = valueX(input)
print(X)

def drawScreen():
    screenstring = ''
    for i in range(6):
        for j in range(40):
            if abs(j-X[j+i*40]) <= 1:
                print(j-X[j+i*40])
                screenstring += '#'
            else:
                screenstring += '.'
            #do nothing
        screenstring += '\n'
    print(screenstring)

drawScreen()