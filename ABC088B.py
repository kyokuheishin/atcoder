import io
import sys

# input here
_INPUT = """\
4
20 18 2 18
"""
sys.stdin = io.StringIO(_INPUT)

###########################CODE#######################

n = int(input())
cards = list(map(int,input().split()))
cards.sort()

score_a = 0
score_b = 0

for i,v in enumerate(cards):
  if i % 2 == 0:
    score_a += v
  else:
    score_b += v

print(abs(score_a-score_b))