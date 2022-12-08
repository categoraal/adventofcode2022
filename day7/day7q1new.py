input = open('day7/input7.txt').read().split('\n')
input = [[col for col in row.split(' ')] for row in input]

def finddirectories(x):
    directoriesindex = []
    for i in range(len(x)):
        if x[i][1] == 'cd' and x[i][2] != '..':
            directoriesindex.append(i)
    return directoriesindex

directories = finddirectories(input)
print(len(directories))

for i in range(len(input))[::-1]: #main loop
    for j in range(len(directories))[::-1]:
        directories[j]
        
    #print(input[i])
    #do loop
    try:
        a = int(input[i][0])
        #print(a)
    except:
        #print('nan')
        a = 0

