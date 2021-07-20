import io
import sys


# input here
_INPUT = """\
10010010

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    n = len(S)

    typea = ["0" if i % 2 == 0 else "1" for i in range(n)]
    typeb = ["1" if i % 2 == 0 else "0" for i in range(n)]

    resa = 0
    resb = 0

    for i in range(n):
        if S[i] != typea[i]:
            resa += 1
        if S[i] != typeb[i]:
            resb += 1

    print(min(resa, resb))

    pass


if __name__ == "__main__":
    main()
