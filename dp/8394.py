import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] % 10 + dp[i-2] % 10

print(dp[-1]%10)