import io
import sys


# input here
_INPUT = """\
5
7 2 3 8 5
3
4 2
1 7
4 13


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    T = list(map(int, input().split()))
    m = int(input())
    sumt = sum(T)
    for i in range(m):
        p, x = map(int, input().split())
        print(sumt-T[p-1]+x)
    pass


if __name__ == "__main__":
    main()
