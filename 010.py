import io
import sys
from typing import Collection

# input here
_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
c1 = [0] * (n+1)
c2 = [0] * (n+1)

for i in range(n):
    c, score = map(int, input().split())

    c1[i+1] = c1[i]
    c2[i+1] = c2[i]

    if c == 1:
        c1[i+1] += score
    else:
        c2[i+1] += score


qn = int(input())

for _ in range(qn):
    l, r = map(int, input().split())
    res1 = c1[r]-c1[l-1]
    res2 = c2[r]-c2[l-1]
    print("%d %d" % (res1, res2))
