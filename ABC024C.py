import io
import sys


# input here
_INPUT = """\
4 4
1 2
2 3
3 4
4 1

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    n, m = map(int, input().split())

    g = collections.defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)

    res = 0
    q = collections.deque()
    for i in range(n):

        seen = set()

        seen.add(i)
        q.append(i)
        while q:
            res += 1
            cur = q.popleft()
            for nei in g[cur]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)

    print(res)


if __name__ == "__main__":
    main()
