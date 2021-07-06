import io
import sys


# input here
_INPUT = """\
8 9
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    a, b = map(int, input().split())

    print((b-1+a-2)//(a-1))


if __name__ == "__main__":
    main()
