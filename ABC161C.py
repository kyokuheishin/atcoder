import io
import sys


# input here
_INPUT = """\
2 6
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, k = map(int, input().split())

    t = n % k

    res = min(t, k-t)
    print(res)
    pass


if __name__ == "__main__":
    main()
