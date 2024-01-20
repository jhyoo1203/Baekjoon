import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0]
tmp = 0

for i in nums:
    tmp += i
    pre.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(pre[j] - pre[i - 1])
