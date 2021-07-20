import io
import sys


# input here
_INPUT = """\
31415 92653

"""
sys.stdin = io.StringIO(_INPUT)


def is_para(num):

    num = str(num)

    l = 0
    r = len(num) - 1

    while l < r:
        if num[l] != num[r]:
            return False
        l += 1
        r -= 1

    return True


def main():
    a, b = map(int, input().split())
    res = 0

    for num in range(a, b+1):
        if is_para(num):
            res += 1
    print(res)
    pass


if __name__ == "__main__":
    main()
