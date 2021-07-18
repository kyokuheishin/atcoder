import io
import sys


# input here
_INPUT = """\
6 3 4
3
1
3
2

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, k, q = map(int, input().split())

    scores = [0] * n

    for _ in range(q):
        scores[int(input())-1] += 1

    for i in range(n):
        if k - q + scores[i] > 0:
            print("Yes")
        else:
            print("No")

    pass


if __name__ == "__main__":
    main()
