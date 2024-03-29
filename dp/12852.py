import sys
input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]
res = [i for i in range(N+1)]
dp[1] = 0
res[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    res[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        res[i] = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        res[i] = i//3

print(dp[N])
print(N, end=' ')

target = N
while res[target] != 0:
    print(res[target], end=' ')
    target = res[target]
