import io
import sys


# input here
_INPUT = """\
1
1


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    A = list(map(int, input().split()))

    gmin = float("inf")

    res = 0

    for num in A:
        if num <= gmin:
            res += 1
        gmin = min(gmin, num)

    print(res)

    pass


if __name__ == "__main__":
    main()
