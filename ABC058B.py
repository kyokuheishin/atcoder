import io
import sys


# input here
_INPUT = """\
atcoderbeginnercontest
atcoderregularcontest


"""
sys.stdin = io.StringIO(_INPUT)


def main():
    O = list(reversed(input()))
    E = list(reversed(input()))

    res = []

    i = 0

    while i < 52 and (O != [] or E != []):
        if i % 2 == 0:
            res.append(O.pop())
        else:
            res.append(E.pop())
        i += 1
    print("".join(res))

    return


if __name__ == "__main__":
    main()
