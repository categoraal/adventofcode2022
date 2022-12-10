input = open('day10/input10.txt').read().split('\n')
input = [row.split(' ') for row in input]

def valueX(input):
    instruction = [1]
    for i in range(len(input)):
        instruction.append(instruction[-1]) 
        if input[i][0] != 'noop':
            instruction.append(instruction[-1] + int(input[i][1]))
    return instruction

def drawScreen(X):
    screenstring = ''
    for i in range(6):
        for j in range(40):
            if abs(j-X[j+i*40]) <= 1:
                screenstring += '#'
            else:
                screenstring += '.'
        screenstring += '\n'
    print(screenstring)

drawScreen(valueX(input))