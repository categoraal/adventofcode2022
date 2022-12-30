import re

input = open('day21/input21.txt').read().strip().split('\n')
input = [x.replace(':','').split(' ') for x in input]
names = [x[0] for x in input]

monkeyNumber = [] #list with all monkey, and path to human
def monkeynumber(monkey):
    #print(monkey)
    flag = 0
    if monkey == 'humn':
        flag = 1
    result = 0
    place = names.index(monkey)
    if input[place][1].isdigit():
        result = int(input[place][1])
    else:
        left,flagleft = monkeynumber(input[place][1])
        right,flagright = monkeynumber(input[place][3])
        if input[place][2] == '+':
            result = left + right
        elif input[place][2] == '-':
            result = left - right
        elif input[place][2] == '*':
            result= left * right
        elif input[place][2] == '/':
            result = left / right
        flag = flagright+flagleft
    monkeyNumber.append([monkey, result, flag])
    return result,flag

monkeynumber('root')
monkeyNumberindex = [x[0] for x in monkeyNumber]

def Human(monkey,num):
    res = 0
    place = names.index(monkey)
    if input[place][1].isdigit() == False:
        monkeyL = input[place][1]
        monkeyR = input[place][3]
        mli = monkeyNumberindex.index(monkeyL)
        mri = monkeyNumberindex.index(monkeyR)
        if monkey == 'root':
            if monkeyNumber[mli][2] == 1:
                monkeyNumber[mli][1] = monkeyNumber[mri][1]
                Human(monkeyNumber[mli][0],monkeyNumber[mri][1])
            else:
                monkeyNumber[mri][1] = monkeyNumber[mli][1]
                Human(monkeyNumber[mri][0],monkeyNumber[mli][1])
        else:
            if monkeyNumber[mli][2] == 1:
                if input[place][2] == '+':
                    monkeyNumber[mli][1] = num - monkeyNumber[mri][1]
                elif input[place][2] == '-':
                    monkeyNumber[mli][1] = num + monkeyNumber[mri][1]
                elif input[place][2] == '*':
                    monkeyNumber[mli][1] = num / monkeyNumber[mri][1] 
                elif input[place][2] == '/':
                    monkeyNumber[mli][1] = num * monkeyNumber[mri][1]
                Human(monkeyNumber[mli][0],monkeyNumber[mli][1])
            else:
                if input[place][2] == '+':
                    monkeyNumber[mri][1] = num - monkeyNumber[mli][1]
                elif input[place][2] == '-':
                    monkeyNumber[mri][1] = monkeyNumber[mli][1] - num
                elif input[place][2] == '*':
                    monkeyNumber[mri][1] = num / monkeyNumber[mli][1]
                elif input[place][2] == '/':
                    monkeyNumber[mri][1] = monkeyNumber[mli][1] / num
                Human(monkeyNumber[mri][0],monkeyNumber[mri][1])
        if monkeyL == 'humn' or monkeyR == 'humn':
            a = monkeyNumberindex.index('humn')
            print(monkeyNumber[a][1])
    return res

Human('root',0)