import io
import sys


# input here
_INPUT = """\
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g##.#.#.#.
###.#.#.#.
###.#.#.#.
#.....#...
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    m, n = map(int, input().split())

    mt = []

    sx, sy = -1, -1
    gx, gy = -1, -1
    for i in range(m):
        line = input()

        if sx == -1 or gx == -1:
            for j in range(n):
                if line[j] == "s":
                    sx, sy = i, j
                elif line[j] == "g":
                    gx, gy = i, j
        mt.append(list(line))
    # print((gx, gy))
    q = collections.deque([(sx, sy, 0)])
    # print(mt)
    mt[sx][sy] = "X"

    while q:
        x, y, c = q.popleft()

        for d in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx = x+d[0]
            ny = y+d[1]

            if 0 <= nx < m and 0 <= ny < n:
                if mt[nx][ny] == "g":
                    print("YES")
                    return
                if mt[nx][ny] == "#":
                    if c < 2:
                        mt[nx][ny] = 'X'
                        q.append((nx, ny, c+1))
                if mt[nx][ny] == ".":
                    mt[nx][ny] = 'X'
                    q.appendleft((nx, ny, c))

    print("NO")
    return


if __name__ == "__main__":
    main()
