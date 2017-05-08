import sys

n = raw_input()
trial = raw_input()

if int(n) >= 1 and int(n) <= 1000000:
    cont = 0
    aux = 0
    for i in trial:
        var = int(i)
        if var == 6:
            cont += 1
        if cont > 3:
            aux += 1
            cont = 0
    print aux
else:
    sys.exit()
