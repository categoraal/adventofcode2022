input = open('day2/input2.txt').read()

games = input.split('\n')
score = 0

for i in range(len(games)):
    if games[i] == "A X" or games[i] == "B Y" or  games[i] == "C Z":
        score += 3
    elif games[i] == "A Y" or games[i] == "B Z" or games[i] == "C X":
        score += 6    
    if games[i][2] == 'X':
        score += 1
    elif games[i][2] == 'Y':
        score += 2
    else:
        score += 3
    
print(score)