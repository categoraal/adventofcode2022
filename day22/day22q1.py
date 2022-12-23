#start leftmost open tile   -x <--- ----> x   y v & ^ -y
#stop at wall
import re
input = open('day22/input22test.txt').read()
board,moves = input.split('\n\n')
board = board.split('\n')
distances = [int(x) for x in re.findall(r'\d+',moves)]
directions = re.findall(r'\D',moves)

print(directions)
startx = (board[0].index('.'))
starty = 0
direction = (1,0),(0,1),(-1,0),(0,-1)

print(direction[0])



#for i in range(len(distances)):
#    print(i)