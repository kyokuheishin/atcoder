import io
import sys


# input here
_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    res = 1
    a, b = map(int, input().split())

    while (a*2 <= b):
        a *= 2
        res += 1
    print(res)


if __name__ == "__main__":
    main()
