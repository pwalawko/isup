import sys


def counting(a1, r, n):
    try:
        a1 = int(a1)
        n = int(n)
        r = int(r)
    except ValueError:
        print('Incorrect parameter!')
    else:
        print(a1 + (n - 1) * r)

if __name__ == '__main__':
    try:
        a1 = sys.argv[1]
        n = sys.argv[3]
        r = sys.argv[2]
    except IndexError:
        print('Parameter missing!')
    else:
        counting(a1, r, n)
