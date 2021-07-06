import io
import sys

# input here
_INPUT = """\
2
5 1 1
100 1 1



"""
sys.stdin = io.StringIO(_INPUT)

###########################CODE#######################



res = [-1,-1,-1]
def main():
  n = int(input())
  lt,lx,ly = 0,0,0
  for _ in range(n):
    t,x,y = map(int,input().split())
    distance = abs(x-lx)+abs(y-ly)
    dtime = abs(t-lt)
    if distance > dtime:
      print("No")
      return
    if dtime % 2 != distance % 2:
      print("No")
      return
    lt,lx,ly = t,x,y
  print("Yes")
  return
main()