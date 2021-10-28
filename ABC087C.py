import io
import sys


# input here
_INPUT = """\
7
3 3 4 5 4 5 3
5 3 4 4 2 3 2

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [list(map(int, input().split())), list(map(int, input().split()))]

    dp = [[0 for _ in range(N)], [0 for _ in range(N)]]

    dp[0][0] = A[0][0]

    dp[1][0] = A[1][0] + dp[0][0]

    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + A[0][j]

    for i in range(1, 2):
        for j in range(1, N):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + A[i][j]

    print(dp[-1][-1])

    return


if __name__ == "__main__":
    main()
