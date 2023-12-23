import sys

input = sys.stdin.readline().strip()
n, k, x = map(int, input.split())

arr = [0] * n
dp = [[False] * (x * k + 1) for _ in range(k + 1)]

for i in range(n):
    input = sys.stdin.readline().strip()
    a, b = map(int, input.split())
    arr[i] = a

for p in arr:
    for i in range(k - 1, 0, -1):
        for j in range(x * k, p - 1, -1):
            dp[i + 1][j] = dp[i + 1][j] or dp[i][j - p]

    dp[1][p] = True

res = 0
for i in range(x * k + 1):
    if dp[k][i]:
        res = max(res, i * (x * k - i))

print(res)
