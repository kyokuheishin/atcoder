import io
import sys


# input here
_INPUT = """\
10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    d = collections.defaultdict(list)

    N = int(input())

    for i in range(N):
        line = list(input().split())
        S = line[0]
        P = int(line[1])

        d[S].append((P, i+1))

    for key in sorted(d.keys()):
        for P, i in sorted(d[key], key=lambda x: -x[0]):
            print(i)

    return


if __name__ == "__main__":
    main()
