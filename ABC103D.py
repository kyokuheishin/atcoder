import io
import sys


# input here
_INPUT = """\
9 5
1 8
2 7
3 5
4 6
7 9

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from operator import itemgetter

    n, m = map(int, input().split())

    ab = sorted([tuple(map(int, input().split()))
                for _ in range(m)], key=lambda x: x[1])

    removed = -1
    ans = 0

    for a, b in ab:

        if a > removed:
            removed = b - 1
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
