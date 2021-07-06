import io
import sys


# input here
_INPUT = """\
99992
"""
sys.stdin = io.StringIO(_INPUT)


def main():

    table = [True] * 1000001
    table[0] = False
    table[1] = False

    for i in range(2, 1000001):
        if table[i]:
            for j in range(i+i, 1000001, i):
                table[j] = False

    x = int(input())

    for i in range(x, 1000001):
        if table[i]:
            print(i)
            return

    pass


if __name__ == "__main__":
    main()
