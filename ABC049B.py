import io
import sys


# input here
_INPUT = """\
9 20
.....***....***.....
....*...*..*...*....
...*.....**.....*...
...*.....*......*...
....*.....*....*....
.....**..*...**.....
.......*..*.*.......
........**.*........
.........**.........

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())

    origin = []

    for _ in range(H):
        origin.append(input())

    res = [["" for _ in range(W)] for _ in range(2*H)]

    for i in range(2*H):
        for j in range(W):
            res[i][j] = origin[int((i)//2)][j]

    for i in range(2*H):
        print("".join(res[i]))

    return


if __name__ == "__main__":
    main()
