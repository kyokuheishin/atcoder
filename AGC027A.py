import io
import sys


# input here
_INPUT = """\
2 10
20 20

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    res = 0
    for i, a in enumerate(A):
        if x >= a:

            if i != n-1:
                x -= a
                res += 1

            else:
                if x == a:
                    res += 1
        else:
            break

    print(res)

    pass


if __name__ == "__main__":
    main()
