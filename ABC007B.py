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


def main():
    s = input()

    if len(s) == 1 and s[0] == "a":
        print(-1)
        return
    print("a")


if __name__ == "__main__":
    main()
