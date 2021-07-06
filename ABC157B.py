import io
import sys


# input here
_INPUT = """\
60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    mat = []
    stamp = [[False for _ in range(3)] for _ in range(3)]
    for i in range(3):
        line = list(map(int, input().split()))
        mat.append(line)
    n = int(input())
    seen = set()
    for _ in range(n):
        seen.add(int(input()))
    for i in range(3):
        for j in range(3):
            if mat[i][j] in seen:
                stamp[i][j] = True

    for i in range(3):
        if all(stamp[i]):
            print("Yes")
            return
    for j in range(3):
        tmp = []
        for i in range(3):
            tmp.append(stamp[i][j])
        if all(tmp):
            print("Yes")
            return

    t1 = [stamp[0][0], stamp[1][1], stamp[2][2]]
    if all(t1):
        print("Yes")
        return
    t2 = [stamp[0][2], stamp[1][1], stamp[2][0]]
    if all(t2):
        print("Yes")
        return
    print("No")
    return

    pass


if __name__ == "__main__":
    main()
