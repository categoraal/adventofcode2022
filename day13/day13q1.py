import json
input = open('day13/input13.txt').read().strip().split('\n\n')
input = [x.split('\n') for x in input]

def compare(left,right):
    res = None
    lengths = [len(left),len(right)]
    for i in range(max(lengths)):
        if i == lengths[0]:
            return 1
        if i == lengths[1]:
            return 0
        
        if type(left[i]) == type(right[i]) and type(left[i])==int:
            if left[i] < right[i]:
                return 1
            if left[i] > right[i]:
                return 0
        if type(left[i]) == type(right[i]) and type(left[i])==list:
            res = compare(left[i],right[i])
        if type(left[i]) == int and type(right[i]) == list:
            res = compare([left[i]],right[i])
        if type(left[i]) == list and type(right[i]) == int:
            res = compare((left[i]),[right[i]])
        if res != None:
            return res

sum = 0
for i in range(len(input)):
    check = (compare(json.loads(input[i][0]),json.loads(input[i][1])))
    if check == 1:
        sum += (i+1)
print('sum =',sum)