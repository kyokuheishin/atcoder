import io
import sys


# input here
_INPUT = """\
aaaaaaaaaaaaaaab
aaaaaaaaaaaaaaab


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    S = list(input())
    T = list(input())

    n = len(S)

    for _ in range(n):
        S.append(S.pop(0))

        if S == T:
            print("Yes")
            return

    print("No")

    return


if __name__ == "__main__":
    main()
