import io
import sys


# input here
_INPUT = """\
50 50
2 2
49 49
##################################################
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
##################################################



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    import collections

    mt = []
    seen = set()
    m, n = map(int, input().split())
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    gx, gy = map(int, input().split())
    gx -= 1
    gy -= 1
    q = collections.deque([(sx, sy, 0)])
    seen.add((sx, sy))
    for _ in range(m):

        line = list(input())
        mt.append(line)

    while q:
        x, y, steps = q.popleft()
        if (x, y) == (gx, gy):
            print(steps)
            return

        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx = x+d[0]
            ny = y+d[1]

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and mt[nx][ny] != "#":
                seen.add((nx, ny))
                q.append((nx, ny, steps+1))

    return


if __name__ == "__main__":
    main()
