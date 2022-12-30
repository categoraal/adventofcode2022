input = open('day25/input25.txt').read().strip().splitlines()
print(input)
#2,1,0,-1,-2  pental system

def lookup(x):
    match x:
        case '2':
            return 2
        case '1':
            return 1
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2

def StoD(snafu):
    decimal = 0
    depth = len(snafu)
    for i in range(depth):
        dec = lookup(snafu[i])
        decimal += 5**(depth-1-i)*dec

    return decimal

def DtoS(decimal):
    snafu = '2'
    while StoD(snafu) < decimal:
        snafu += '2'
    print(snafu)
    for p in range(0, len(snafu)):
        for new_digit in ['1', '0', '-', '=']:
            new_s = snafu[0:p] + new_digit + snafu[p+1:len(snafu)]
            if StoD(new_s) >= decimal:
                snafu = new_s
    
    return snafu


sum = 0
for i in input:
    sum += StoD(i)

print(sum)

print(DtoS(sum))