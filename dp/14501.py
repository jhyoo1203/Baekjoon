import sys

input = sys.stdin.readline

N = int(input())
T = list()
P = list()
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if T[i] + i <= N:
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
