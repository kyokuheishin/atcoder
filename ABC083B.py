import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

###########################CODE#######################

def helper(num):
  res = 0
  num = str(num)
  for i in range(len(num)):
    res += int(num[i])
  return res

n,a,b = map(int,input().split())

res = 0
for num in range(1,n+1):
    if a <= helper(num) <= b:
        res += num
print(res)