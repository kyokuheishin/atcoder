import io
import sys


# input here
_INPUT = """\
10
2184 2126 1721 1800 1024 2528 3360 1945 1280 1776


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0

    for i in range(n):
        tmp = A[i]

        while tmp % 2 == 0:
            tmp = tmp // 2
            res += 1
    print(res)
    return


if __name__ == "__main__":
    main()
