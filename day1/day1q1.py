input = open("day1/input1.txt","r")

input = input.read() #string input
lists = input.split('\n\n') #lists

b = [0]*len(lists)
for i in range(len(lists)-1):
    var = lists[i].split('\n')
    array = [0]*len(var)
    for j in range(len(var)):
        array[j] = int(var[j])
    b[i] = sum(array)

b.sort(reverse=True)

listlength = len(b)
result = b[0]+b[1]+b[2]
print(b[0], result)
