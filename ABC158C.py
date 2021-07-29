import io
import sys


# input here
_INPUT = """\
2 2




"""
sys.stdin = io.StringIO(_INPUT)


def main():
    a, b = map(int, input().split())
    res = float("inf")

    for num1 in range(1, 10001):

        if int(num1*0.08) == a and int(num1*0.10) == b:
            print(num1)
            return

    print(-1)
    return

    pass


if __name__ == "__main__":
    main()
