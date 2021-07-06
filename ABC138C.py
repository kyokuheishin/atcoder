import io
import sys


# input here
_INPUT = """\
2
3 4


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import heapq
    n = int(input())
    A = list(map(int, input().split()))

    # res = 0

    heapq.heapify(A)
    for i in range(n-1):
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        tmp = (a+b) / 2
        heapq.heappush(A, tmp)

    print(heapq.heappop(A))
    pass


if __name__ == "__main__":
    main()
