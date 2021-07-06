import io
import sys


# input here
_INPUT = """\
14
99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    a = A[n//2]
    b = A[n//2-1]

    print(abs(a-b))
    pass


if __name__ == "__main__":
    main()
