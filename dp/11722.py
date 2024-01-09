import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sort_A = list(reversed(A))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if sort_A[i] > sort_A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
