import io
import sys


# input here
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cur = 1

    for num in A:
        if num == cur:
            cur += 1

    if cur == 1:
        print("-1")
    else:
        print(N-cur+1)

    return


if __name__ == "__main__":
    main()
