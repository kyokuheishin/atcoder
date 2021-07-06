
import collections
import io
import sys

# input here
_INPUT = """\
1 10
s..####..g




"""
sys.stdin = io.StringIO(_INPUT)


def main():

    m, n = map(int, input().split())

    matrix = [["" for _ in range(n)] for _ in range(m)]
    start = (-1, -1)
    for i in range(m):
        line = input()
        for j in range(n):
            matrix[i][j] = line[j]
            if line[j] == "s":
                start = (i, j)

        matrix.append(line)
    seen = set()
    queue = collections.deque([start])

    while queue:
        node = queue.pop()
        x = node[0]
        y = node[1]

        seen.add((x, y))

        if matrix[x][y] == "g":
            print("Yes")
            return
        else:
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x+d[0]
                ny = y+d[1]

                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != "#" and (nx, ny) not in seen:
                    queue.append((nx, ny))

    print("No")


main()
