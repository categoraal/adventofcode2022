import json
input = open('day13/input13.txt').read().strip().replace('\n\n','\n').split('\n')
input.append('[[2]]')
input.append('[[6]]')
input = [json.loads(x) for x in input]

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

def bubblesort(unsortedList):
    n = len(unsortedList)
    swapped = False
    for i in range(n-1):
        if compare(unsortedList[i],unsortedList[i+1]) != 1:
            swapped = True
            unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i]
    return swapped

res = True
while res == True:
    res = bubblesort(input)

print('the product of the indices =', (input.index([[2]])+1)*(input.index([[6]])+1))