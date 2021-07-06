import io
import sys


# input here
_INPUT = """\
10 7 5
1 2 3 4 6 8 9


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, m, x = map(int, input().split())
    x -= 1
    A = [0] * n
    targets = list(map(int, input().split()))
    for target in targets:
        A[target-1] = 1
    res = min(sum(A[:x+1]), sum(A[x:]))
    print(res)
    pass


if __name__ == "__main__":
    main()
