input = open('day11/input11test.txt').read()
input = input.split('\n\n')
print(len(input))
input = [x.split('\n') for x in input]
print(input)