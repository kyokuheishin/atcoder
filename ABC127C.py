import io
import sys


# input here
_INPUT = """\
4 2
1 3
2 4

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, m = map(int, input().split())
    l = 1
    r = n
    for _ in range(m):
        a, b = map(int, input().split())
        l = max(l, a)
        r = min(r, b)

    print(max(0, r-l+1))
    return


if __name__ == "__main__":
    main()
