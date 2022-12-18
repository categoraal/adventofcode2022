input = open('day17/day17file.txt').read().strip().split('\n')
input = [int(x) for x in input]
print(input[:10])
lengths = []
for i in range(len(input)-1):
    lengths.append(input[i+1]-input[i])
def finder():
    for i in range(len(lengths)-1000):
        for j in range(i+1,len(lengths)-1000):
            if lengths[i:i+100] == lengths[j:j+100]:
                print(i,j)
                return i,i-j

print(finder())
                   