import sys

input = sys.stdin.readline

N = int(input())
place = [int(input()) for _ in range(N)]
place.sort()
res = 0

for i in range(N):
    res += abs(i-place[i] + 1)

print(res)