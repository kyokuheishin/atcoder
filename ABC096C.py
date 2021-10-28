import io
import sys


# input here
_INPUT = """\
1500 2000 500 90000 100000

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    A, B, C, X, Y = map(int, input().split())
    res = float("inf")

    for num in range(0, 201010):
        tmp = C * num

        x = X - num // 2
        y = Y - num // 2

        if 0 < x:
            tmp += x*A
        if 0 < y:
            tmp += y*B
        res = min(res, tmp)

    print(res)
    return


if __name__ == "__main__":
    main()
