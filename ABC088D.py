import io
import sys


# input here
_INPUT = """\
10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
.....................................

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections
    m, n = map(int, input().split())
    blacks = 0
    res = -1
    mat = []
    for i in range(m):
        line = input()
        for j in range(n):
            if line[j] == "#":
                blacks += 1
        mat.append(list(line))
    q = collections.deque([(0, 0, 1)])
    seen = set()
    seen.add((0, 0))

    while q:
        x, y, steps = q.popleft()
        if (x, y) == (m-1, n-1):
            res = steps
            break
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+d[0], y+d[1]

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and mat[nx][ny] != "#":
                seen.add((nx, ny))
                q.append((nx, ny, steps+1))
    if res == -1:
        print(-1)
    else:
        print(m*n-res-blacks)


if __name__ == "__main__":
    main()
