input = open('day3/input3.txt').read().split('\n')

valuePairs = {'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def badge(x):
    overlapping = []
    for i in range(len(x[0])):
        for j in range(len(x[1])):
            if x[0][i] == x[1][j]:
                overlapping.append(x[0][i])
                for k in range(len(x[2])):
                    if x[0][i] == x[2][k]:
                        return x[0][i]

sum = 0
for i in range(int(len(input)/3)):
    sum += int(valuePairs.get(badge(input[i*3:i*3+3])))

print('The value = ',sum)