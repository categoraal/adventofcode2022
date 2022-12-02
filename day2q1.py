input = open('input2.txt').read()

games = input.split('\n')
print(games[0][2])
score = 0
sum = 0
for i in range(len(games)):
    if games[i] == "A X" or games[i] == "B Y" or  games[i] == "C Z":
        score += 3
        print(games[i])
        sum += 1
    elif games[i] == "A Y" or games[i] == "B Z" or games[i] == "C X":
        score += 6
        print('Win')
    else:
        print('lose')
    
    if games[i][2] == 'X':
        score += 1
    elif games[i][2] == 'Y':
        score += 2
    else:
        score += 3
    

print(score)
print(sum)
print(type(games[0]))
#A, X, rock. B,Y, scissors, C,Z, paper
#'A X','A Y','A Z',