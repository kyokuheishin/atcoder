import io
import sys


# input here
_INPUT = """\
fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg



"""
sys.stdin = io.StringIO(_INPUT)


def main():

    seen = [0] * 26

    s = input()

    for c in s:
        seen[ord(c)-97] = 1

    for i in range(26):
        if seen[i] == 0:
            print(chr(97+i))
            return
    print("None")
    return

    pass


if __name__ == "__main__":
    main()
