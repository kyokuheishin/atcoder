import io
import sys


# input here
_INPUT = """\
2 9 100

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    a, b, k = map(int, input().split())

    upper = a + k - 1
    lower = b - k + 1

    for num in range(a, b+1):
        if num <= upper or num >= lower:
            print(num)

    pass


if __name__ == "__main__":
    main()
