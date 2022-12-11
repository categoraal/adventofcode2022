input = open('day7/input7.txt').read().split('\n')
input = [[col for col in row.split(' ')] for row in input]

#def findcddirectories(x):
#    directoriesindex = []
#    for i in range(len(x)):
#        if x[i][1] == 'cd' and x[i][2] != '..':
#            directoriesindex.append(i)
#    return directoriesindex

def finddirectories(x):
    directories = []
    for i in range(len(x)):
        if x[i][0] == 'dir':
            directories.append(i)
            directories.append(x[i][1])
    return list(reversed(directories))

directories = finddirectories(input)
print(directories)
#cddirectories = findcddirectories(input)
#print(len(directories))

directorieSize = 0
sizes = []
for i in range(len(input))[::-1]: #main loop
    #print(type(input[i][0]),i)
    if input[i][0].isdigit():
        directorieSize += int(input[i][0])
    if input[i][1] == 'cd' and input[i][2] != '..' and input [i][2] != '/' and input[i][0] == '$':
        sizes.append(directorieSize)
        a = directories.index(input[i][2])
        #print(a, directories[a:a+2])
        input[directories[a+1]][0] = str(directorieSize)
        del directories[a+1]
        del directories[a]
        directorieSize = 0
        #print(input)
        #directorie = directorieSize
print(directories)
#sizes.sort()
#print(sizes)
#print(input)
result = (x for x in sizes if x < 100000)
print(sum(result))
