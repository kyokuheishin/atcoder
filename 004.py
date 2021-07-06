
import io
import sys
from typing import Collection

# input here
_INPUT = """\
4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
"""
sys.stdin = io.StringIO(_INPUT)


m, n = map(int, input().split())

matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))

drow = [0] * m
dcol = [0] * n

for i in range(m):
    for j in range(n):
        num = matrix[i][j]
        drow[i] += num
        dcol[j] += num

for i in range(m):
    for j in range(n):
        matrix[i][j] = str(drow[i] + dcol[j] - matrix[i][j])

for line in matrix:
    print(" ".join(line))
