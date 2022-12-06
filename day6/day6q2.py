input = open('day6/input6.txt').read()
print(len(input))

def overlapping(x):
    a = 0
    z = len(x)
    for i in range(z-1):
        for j in range(z-i-1):
            if x[i] == x[i+j+1]:
                a += 1
    return a

for i in range(len(input)-14):
    res = overlapping(input[i:i+14])
    if res == 0:
        print('the result is', i+14)
        break