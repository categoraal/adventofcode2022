input = open('day7/input7.txt').read().split('\n')
input = [[col for col in row.split(' ')] for row in input]

#def isDirectory(x):
#    res = False
#    if x[1] == 'ls':
#        res = True
#    return res

sum = 0
for i in range(len(input)):
    if input[i][0] == 'dir':
        sum += 1
print(sum)

def findLowestDirectoryRange(x): #find the lowest directory in the nested structure
    for i in range(len(x)):  # type: ignore
        if x[i][1] == 'ls': #here begins a list
            a = i
        if (x[i][1] == 'cd' and x[i][2] == '..'):
            b = i
            break
    return a, b

def sizeOfDirectory(x):
    sum = 0
    for i in x:  # type: ignore
        sum += int(i[0])
    return sum

def removeDir(oldlist, dir):
    a = oldlist[dir[0]-1][2]
    del oldlist[dir[0]-1:dir[1]+1]
    return a
#list directories

def findSpecificDir(inputList, name):
    for i in range(len(inputList)):  # type: ignore
        if inputList[i][1] == name:
            return i
            break

def replaceDir(inputlist, index, number):
    inputlist[index][0] = number

#res = findLowestDirectoryRange(input)
#print(res)

#a = sizeOfDirectory(input[res[0]+1:res[1]])
#print(a)

#a = removeDir(input, res)
#print(a)

#print(findSpecificDir(input, a))
directorySize = []
for i in range(len(input)):
    range = findLowestDirectoryRange(input)
    size = sizeOfDirectory(input[range[0]+1:range[1]])
    name = removeDir(input, range)
    directorySize.append(size)
    print(type(input))
    index = findSpecificDir(input, name)
    replaceDir(input, index, size)
