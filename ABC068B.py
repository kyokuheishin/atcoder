import io
import sys


# input here
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    bn = bin(n)[2:]
    tmp = '1' + ('0' * (len(bn)-1))
    print(int(tmp, 2))
    pass


if __name__ == "__main__":
    main()
