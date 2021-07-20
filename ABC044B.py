import io
import sys


# input here
_INPUT = """\
abaccaba

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections

    d = collections.Counter(list(input()))

    for key in d:
        if d[key] % 2:
            print("No")
            return
    print("Yes")
    pass


if __name__ == "__main__":
    main()
