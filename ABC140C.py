import io
import sys


# input here
_INPUT = """\
6
0 153 10 10 23

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    B = list(map(int, input().split()))

    res = [0] * n
    res[0] = B[0]
    res[-1] = B[-1]
    for i in range(1, n-1):
        res[i] = min(B[i], B[i-1])

    print(sum(res))
    pass


if __name__ == "__main__":
    main()
