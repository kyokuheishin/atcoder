import io
import sys


# input here
_INPUT = """\
HASFJGHOGAKZZFEGA



"""
sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()

    l = 0
    r = len(S)-1

    while l < r:
        if S[l] != "A":
            l += 1
        if S[r] != "Z":
            r -= 1

        if S[l] == "A" and S[r] == "Z":
            print(r-l+1)
            return

    return


if __name__ == "__main__":
    main()
