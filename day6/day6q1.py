input = open('day6/input6.txt').read()
print(len(input))
print(input[0:4])

for i in range(len(input)-4):
    a = input[i:i+4]
    if a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]:
        print(i+4)
        print(a)
        break