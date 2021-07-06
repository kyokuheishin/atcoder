import collections
import io
import sys

# input here
_INPUT = """\
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
ooooxooooo
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx




"""
sys.stdin = io.StringIO(_INPUT)


def helper(i, j, matrix, seen, m, n):
    res = 1
    seen.add((i, j))
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x = i+d[0]
        y = j+d[1]

        if 0 <= x < m and 0 <= y < n and matrix[x][y] == "o" and (x, y) not in seen:
            res += helper(x, y, matrix, seen, m, n)
    return res


def main():
    lands = 0
    matrix = []

    m = 10
    n = 10

    for _ in range(m):
        tmp = []
        line = input()
        for c in line:
            if c == "o":
                lands += 1
            tmp.append(c)
        matrix.append(tmp)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "x":
                res = helper(i, j, matrix, set(), m, n)
                if res == lands + 1:
                    print("YES")
                    return
    print("NO")
    return


main()
