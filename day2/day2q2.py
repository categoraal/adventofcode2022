input = open('day2/input2.txt').read().split('\n')

score = 0
for i in range(len(input)):
    if input[i] == 'A X':
        score += 3
    elif input[i] == 'A Y':
        score += 4       
    elif input[i] == 'A Z':
        score += 8
    elif input[i] == 'B X':
        score += 1
    elif input[i] == 'B Y':
        score += 5
    elif input[i] == 'B Z':
        score += 9
    elif input[i] == 'C X':
        score += 2
    elif input[i] == 'C Y':
        score += 6
    else:
        score += 7

print('score is', score)