import io
import sys


# input here
_INPUT = """\
8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    d = collections.defaultdict(lambda: 0)
    n, m = map(int, input().split())

    for _ in range(m):
        a, b = map(int, input().split())
        d[a] += 1
        d[b] += 1
    for i in range(1, n+1):
        print(d[i])

    pass


if __name__ == "__main__":
    main()
