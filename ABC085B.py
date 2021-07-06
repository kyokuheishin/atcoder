import io
import sys

# input here
_INPUT = """\
4
10
8
8
6


"""
sys.stdin = io.StringIO(_INPUT)

###########################CODE#######################

n = int(input())
mochi = set()
for _ in range(n):
  mochi.add(int(input()))
print(len(mochi))