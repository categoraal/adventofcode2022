import re
input = open('day15/input15test.txt').read().strip().split('\n')
input = [re.findall(r'[\-]\d+|\d+',i) for i in input]
print(input)

for i in range(20):
    print(i)
    if i == 10:
        break