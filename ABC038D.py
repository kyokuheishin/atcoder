import io
import sys


# input here
_INPUT = """\
4
2 5
3 3
4 5
6 6


"""
sys.stdin = io.StringIO(_INPUT)


def main():

    import bisect

    n = int(input())

    boxes = []

    for _ in range(n):
        boxes.append(tuple(map(int, input().split())))

    boxes.sort(key=lambda x: (x[0], -x[1]))

    INF = 10000000

    dp = [INF for i in range(n+1)]
    for i in range(n):
        dp[bisect.bisect_left(dp, boxes[i][1])] = boxes[i][1]
    print(bisect.bisect_left(dp, INF))

    # print(res)


if __name__ == "__main__":
    main()
