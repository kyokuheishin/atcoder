import io
import sys


# input here
_INPUT = """\
54
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    d = {}

    a = int(input())
    d[a] = 1
    for i in range(2, 1000001):
        if a % 2:
            tmp = 3*a+1

        else:
            tmp = a // 2

        if tmp in d:
            print(i)

            return

        d[tmp] = i
        # print(tmp)
        a = tmp

    pass


if __name__ == "__main__":
    main()
