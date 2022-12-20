import sys

input = sys.stdin.readline

N, M = map(int, input().split())

minPack = 1001
minSingle = 1001
for i in range(M):
  p, s = map(int, input().split())
  minPack = min(minPack, p)
  minSingle = min(minSingle, s)

result = 0

if minPack > minSingle*6:
  result += N * minSingle
else:
  result += (N//6) * minPack
  if (N%6)*minSingle > minPack:
    result += minPack
  else:
    result+= (N%6)*minSingle

print(result)