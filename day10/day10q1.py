input = open('day10/input10.txt').read().split('\n')
input = [row.split(' ') for row in input]

def valueX(input):
    instruction = [1, 1]
    for i in range(len(input)):
        if input[i][0] == 'noop':
            instruction.append(instruction[-1]) 
        if input[i][0] != 'noop':
            instruction.append(instruction[-1]) 
            instruction.append(instruction[-1] + int(input[i][1]))
    return instruction

X = valueX(input)
result = 20*X[20] + 60*X[60] +  100*X[100] + 140*X[140] + 180*X[180] + 220*X[220]
print(result)