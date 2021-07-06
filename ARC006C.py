import io
import sys


# input here
_INPUT = """\
6
5
10
15
20
25
30
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    Q = []

    for i in range(N):
        w = int(input())
        ok = 0
        for j in range(len(Q)):
            if w <= Q[j]:
                ok = 1
                Q[j] = w
                break
        if ok == 0:
            Q.append(w)
        Q.sort()

    print(len(Q))


if __name__ == "__main__":
    main()
