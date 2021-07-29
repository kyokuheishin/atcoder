import io
import sys


# input here
_INPUT = """\
3
abc
arc
agc



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    seen = set()
    n = int(input())
    last = input()
    seen.add(last)

    for _ in range(1, n):
        cur = input()
        if cur[0] != last[-1]:
            print("No")
            return
        else:
            if cur in seen:
                print("No")
                return
            else:
                seen.add(cur)
                last = cur
    print("Yes")
    pass


if __name__ == "__main__":
    main()
