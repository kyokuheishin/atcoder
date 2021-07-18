import io
import sys


# input here
_INPUT = """\
-1 1

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    l, r = map(int, input().split())

    if (l < 0 and r > 0) or l == 0 or r == 0:
        print("Zero")
    if l > 0 and r > 0:
        print("Positive")
    if l < 0 and r < 0:
        if (abs(abs(l)-abs(r))+1) % 2 == 0:
            print("Positive")
        else:
            print("Negative")


if __name__ == "__main__":
    main()
