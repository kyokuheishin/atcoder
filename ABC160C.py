import io
import sys


# input here
_INPUT = """\
20 3
5 10 15

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    k, n = map(int, input().split())
    A = [0] * n

    A = list(map(int, input().split()))

    res = A[n-1] - A[0]

    for i in range(1, n):
        t1 = k - A[i]
        t2 = A[i-1]
        res = min(res, t1+t2)

    print(res)
    pass


if __name__ == "__main__":
    main()
