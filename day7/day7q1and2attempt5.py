input = open('day7/input7.txt').read().split('\n')
input = list(reversed([[col for col in row.split(' ')] for row in input]))
length = len(input)

def findcorrespondingdirecotorie(name, input):
    index = 0
    numcddotdot = 0
    numcdstring = 0
    for i in range(len(input)):
        if input[i][0] == '$' and input[i][1] == 'cd' and input[i][2] == '..':
            numcddotdot += 1
        if input[i][0] == '$' and input[i][1] == 'cd' and input[i][2] != '..':
            numcdstring += 1
        if input[i][0] == 'dir' and input[i][1] == name and numcddotdot == numcdstring:
            index = i-len(input)
            break
    return index

directorieSize = 0
sizes = []
for i in range(len(input)): #main loop
    if input[i][0].isdigit(): #size of a particular directory
        directorieSize += int(input[i][0]) 
    if input[i][1] == 'cd' and input[i][2] != '..' and input [i][2] != '/' and input[i][0] == '$':
        sizes.append(directorieSize) #list with directorie sizes (unorderd and unnamed)
        directorieName = input[i][2]
        index = findcorrespondingdirecotorie(directorieName,input[i+1:])
        input[index][0] = str(directorieSize)
        directorieSize = 0

result = (x for x in sizes if x < 100000)
print(sum(result))

sizeHome = 0
for i in range(len(input)):
    if input[-i-3][0].isdigit():
        sizeHome += int(input[-i-3][0])      
    else:
        break

result2 = [x for x in sizes if x > (sizeHome-40000000)]
print(min(result2))