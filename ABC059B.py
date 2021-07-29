import io
import sys


# input here
_INPUT = """\
123456789012345678901234567890
234567890123456789012345678901

"""
sys.stdin = io.StringIO(_INPUT)


def main():
    a = input()
    b = input()

    if len(a) > len(b):
        print("GREATER")
        return
    elif len(a) < len(b):
        print("LESS")
        return
    else:
        for i in range(len(a)):
            if ord(a[i]) > ord(b[i]):
                print("GREATER")
                return
            elif ord(a[i]) < ord(b[i]):
                print("LESS")
                return
        print("EQUAL")
        return

    pass


if __name__ == "__main__":
    main()
