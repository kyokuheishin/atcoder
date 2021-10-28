import io
import sys


# input here
_INPUT = """\
999
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    res = 1

    X = int(input())

    for num in range(2, X):
        x = num ** 2
        while x <= X:
            res = max(res, x)
            x *= num
    print(res)


if __name__ == "__main__":
    main()
