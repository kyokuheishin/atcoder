import io
import sys


# input here
_INPUT = """\
8
8 2 7 3 4 5 6 1



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    res = [""] * n

    for i in range(n):
        res[A[i]-1] = str(i+1)
    print(" ".join(res))
    pass


if __name__ == "__main__":
    main()
