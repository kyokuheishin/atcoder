import io
import sys


# input here
_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6
"""
sys.stdin = io.StringIO(_INPUT)


def checker(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


def main():
    a, b = input().split()
    num = int(a+b)
    if checker(num):
        print("Yes")
    else:
        print("No")
    pass


if __name__ == "__main__":
    main()
