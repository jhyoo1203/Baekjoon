import sys

input = sys.stdin.readline

n = int(input())
amount = [0] * 10000
for i in range(n):
    amount[i] = int(input())


dp = [0] * 10000
dp[0] = amount[0]
dp[1] = amount[0] + amount[1]
dp[2] = max(amount[0] + amount[2], amount[1] + amount[2], dp[1])
for i in range(3, n):
    dp[i] = max(amount[i] + dp[i - 2], amount[i] + amount[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))
