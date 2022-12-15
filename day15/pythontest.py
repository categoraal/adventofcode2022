import re
input = open('day15/input15test.txt').read().strip().split('\n')
input = [re.findall(r'[\-]\d+|\d+',i) for i in input]
print(input)
