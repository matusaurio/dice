# Author: Santiago Benalcazar
import itertools
import operator

def exe1(n, trial):
    cont = 0
    out = 0
    for i in trial:
        var = int(i)

        if var == 6:
            cont += 1
        else:
            cont = 0

        if cont == 2:
            out += 1
        elif cont > 2:
            out -= 1

        if out < 0:
            out = 0

    print out
    return


def exe2(n, trial):
    cont = 0
    out = 0

    for i in trial:
        var = int(i)
        if var == 6:
            cont = 0
        else:
            cont += 1
            if cont > out:
                out = cont

    print out
    return


def exe3(n, trial):
    cont = 0
    out = 0
    n = 10

    x = [int(i) for i in trial]
    var = map(list, zip (*(x[i:] for i in range(n))))

    for temp in var:
        for item in temp:
            cont += item
        if cont > out:
            out = cont
        cont = 0

    print out
    return


def exe4(n, trial):
    cont = ''
    out = 0
    res = 0
    temp = []
    data =[]
    aux = []

    for i in trial:
        if i == '5' or i == '6':
            cont += i
        else:
            cont = ''
            out = 0

        if out == 0:
            out = len(cont)

        temp.append(out)

    for i in temp:
        if i == 0:
            res = 0
        else:
            res += i
            data.append(res)

    for k, g in itertools.groupby(enumerate(data), lambda (i, x): i-x):
        out = map(operator.itemgetter(1), g)[-1]
        aux.append(out)

    aux = sorted(aux, reverse=True)
    out = max(aux, key=aux.count)

    print out
    return


def validate(n, trial):
    if int(n) >= 1 and int(n) <= 1000000:
        x = 0
        for i in trial:
            x += 1
        if int(n) == x:
            exe1(n, trial)
            exe2(n, trial)
            exe3(n, trial)
            exe4(n, trial)
        else:
            exit()
    else:
        exit()
    return


n = raw_input()
trial = raw_input()

validate(n, trial)
