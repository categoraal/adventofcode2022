input = open('day20/input20.txt').read().strip().split('\n')
key = 811589153
input = [[int(x)*key] for x in input]

for i in range(len(input)):
    input[i].append(i)

for i in range(len(input)*10):
    oldloc = ([x[1] for x in input].index(i%len(input)))
    newloc = (input[oldloc][0] + oldloc)%(len(input)-1)
    input.insert(newloc,input.pop(oldloc))

place = [x[0] for x in input].index(0)
num1 = input[(place+1000)%(len(input))][0]
num2 = input[(place+2000)%(len(input))][0]
num3 = input[(place+3000)%(len(input))][0]

print(num1+num2+num3)