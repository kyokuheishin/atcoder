import io
import sys


# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    a, b, c, k = map(int, input().split())

    if k % 2:
        print(c-b)
    else:
        print(b-c)

    pass


if __name__ == "__main__":
    main()
