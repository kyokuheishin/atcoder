import io
import sys


# input here
_INPUT = """\
1 1
z


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    h, w = map(int, input().split())

    for i in range(h+2):
        if i == 0 or i == h+2-1:
            print("#"*(w+2))
        else:
            print("#"+input()+"#")
    pass


if __name__ == "__main__":
    main()
