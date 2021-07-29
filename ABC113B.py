import io
import sys


# input here
_INPUT = """\
3
21 -11
81234 94124 52141


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    t, a = map(int, input().split())

    H = list(map(int, input().split()))

    res = 1
    dif = float("inf")

    for i in range(n):
        tmp = t-H[i]*0.006
        if abs(a-tmp) < dif:
            res = i + 1
            dif = abs(a-tmp)

    print(res)

    return


if __name__ == "__main__":
    main()
