import io
import sys

_INPUT = """\
11 11
1 2
1 3
2 4
3 5
4 6
5 7
6 8
7 9
8 10
9 11
10 11










"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections

    g = collections.defaultdict(list)

    n, m = map(int, input().split())

    seen = [0] * (n+1)

    res = 0
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1, n+1):
        if seen[i] == 0:
            if helper(g, i, i, seen):

                res += 1

    print(res)


def helper(g, node, prev, seen):

    seen[node] = 2
    for nei in g[node]:
        if seen[nei] == 2 and nei != prev:
            return False
        elif seen[nei] == 1:
            continue
        elif seen[nei] == 0:

            if not helper(g, nei, node, seen):
                return False
    seen[node] = 1
    return True


main()
