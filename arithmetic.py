import sys


def counting():
    try:
        a1 = int(sys.argv[1])
        n = int(sys.argv[3])
        r = int(sys.argv[2])
    except ValueError:
        print('Incorrect parameter!')
    except IndexError:
        print('Parameter missing!')
    else:
        print(a1 + (n-1) * r)

counting()
