import io
import sys


# input here
_INPUT = """\
SHINJUKU



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    s = input()
    res = 0
    n = len(s)
    left = 0
    right = 0
    ok = set()
    ok.add("A")
    ok.add("G")
    ok.add("C")
    ok.add("T")

    while left < n and right < n:
        if s[right] in ok:
            res = max(res, right-left+1)
            right += 1
        else:
            left = right + 1
            right = left
    print(res)
    pass


if __name__ == "__main__":
    main()
