import re

input = open('day21/input21.txt').read().strip().split('\n')
input = [x.replace(':','').split(' ') for x in input]
names = [x[0] for x in input]
#print(len(set([x.split(':')[0] for x in input])))
#print(len(input))
def monkeynumber(monkey):
    result = 0
    place = names.index(monkey)
    #print(place)
    if input[place][1].isdigit():
        result = int(input[place][1])
    elif input[place][2] == '+':
        result = monkeynumber(input[place][1]) + monkeynumber(input[place][3])
    elif input[place][2] == '-':
        result = monkeynumber(input[place][1]) - monkeynumber(input[place][3])
    elif input[place][2] == '*':
        result = monkeynumber(input[place][1]) * monkeynumber(input[place][3])
    elif input[place][2] == '/':
        result = monkeynumber(input[place][1]) / monkeynumber(input[place][3])
    return result

print('the number is:',int(monkeynumber('root')))