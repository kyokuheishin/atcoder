import io
import sys


# input here
_INPUT = """\
1 30
3 5 10 30


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n, m = map(int, input().split())

    d = {}

    for _ in range(n):
        foods = list(map(int, input().split()))[1:]

        for food in foods:
            if food not in d:
                d[food] = 0
            d[food] += 1

    res = 0

    for food in d:
        if d[food] == n:
            res += 1

    print(res)

    pass


if __name__ == "__main__":
    main()
