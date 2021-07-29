import io
import sys


# input here
_INPUT = """\
4
ushi
tapu
nichia
kun



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    N = int(input())

    d = collections.defaultdict(lambda: 0)
    cmax = 0
    for _ in range(N):
        word = input()
        d[word] += 1
        cmax = max(cmax, d[word])

    for key in sorted(d.keys()):
        if d[key] == cmax:
            print(key)

    return


if __name__ == "__main__":
    main()
