import sys


def main():
    try:
        a1 = int(sys.argv[1])
        n = int(sys.argv[3])
        r = int(sys.argv[2])
    except ValueError:
        print('Incorrect parameter!')
    except IndexError:
        print('Parameter missing!')
    else:
        print(counting(a1, r, n))


def counting(a1, r, n):
    assert n >= 0, "Invalid value!"
    return a1 + (n - 1) * r


if __name__ == '__main__':
    main()
