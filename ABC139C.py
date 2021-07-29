import io
import sys


# input here
_INPUT = """\
7
4 4 5 6 6 5 5


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())

    A = list(map(int, input().split()))

    res = 0
    tmp = 0

    for i in range(1, n):
        if A[i] > A[i-1]:
            tmp = 0
        else:
            tmp += 1
            res = max(res, tmp)

    print(res)
    pass


if __name__ == "__main__":
    main()
