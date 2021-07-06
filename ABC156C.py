import io
import sys


# input here
_INPUT = """\
7
14 14 2 13 56 2 37

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())

    a = list(map(int, input().split()))
    res = float("inf")
    for point in range(min(a), max(a)+1):
        tmp = 0
        for num in a:
            tmp += (num-point) ** 2
        res = min(res, tmp)
        pass

    print(res)


if __name__ == "__main__":
    main()
