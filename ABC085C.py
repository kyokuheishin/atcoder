import io
import sys

# input here
_INPUT = """\
2000 20000000
"""
sys.stdin = io.StringIO(_INPUT)

###########################CODE#######################

n,target = map(int,input().split())

res = [-1,-1,-1]
def main(n,target):
  
  for i in range(0,n+1):
    for j in range(0,n+1-i):
      k = n - i - j
      if i*10000 + j*5000 + k*1000 == target:
        print("%d %d %d" % (i,j,k))
        return
  print("-1 -1 -1")
main(n,target)