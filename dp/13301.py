import sys

input = sys.stdin.readline

N = int(input())
dp = [0, 1]

for i in range(2, N + 2):
    dp.append(dp[i - 1] + dp[i - 2])

print((2 * dp[N]) + (2 * dp[N + 1]))
