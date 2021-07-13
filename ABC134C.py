import io
import sys


# input here
_INPUT = """\
2
5
5


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    A = [0] * n
    for i in range(n):
        A[i] = int(input())
    lm = [0] * n
    lm[0] = A[0]
    rm = [0] * n
    rm[-1] = A[-1]
    for i in range(1, n):
        lm[i] = max(A[i], lm[i-1])

    for i in range(n-2, -1, -1):
        rm[i] = max(A[i], rm[i+1])

    for i in range(n):
        if i == 0:
            print(rm[i+1])
        elif i == n-1:
            print(lm[i-1])
        else:
            print(max(rm[i+1], lm[i-1]))
    pass


if __name__ == "__main__":
    main()
