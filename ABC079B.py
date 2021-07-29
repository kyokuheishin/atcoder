import io
import sys


# input here
_INPUT = """\
86
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())

    if n == 0:
        print(2)
        return
    if n == 1:
        print(1)
        return

    dp = [0] * (n+1)
    dp[0] = 2
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-1])

    pass


if __name__ == "__main__":
    main()
