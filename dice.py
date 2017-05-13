import sys

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
    return

def exe3(n, trial):
    return

def exe4(n, trial):
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
            sys.exit()
    else:
        sys.exit()
    return


n = raw_input()
trial = raw_input()

validate(n, trial)
