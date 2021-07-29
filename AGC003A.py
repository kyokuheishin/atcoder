import io
import sys


# input here
_INPUT = """\
NNEW

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    d = collections.Counter(input())

    if len(d) != 4:
        print("No")
    else:
        print("Yes")

    return


if __name__ == "__main__":
    main()
