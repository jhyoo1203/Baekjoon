import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
INF = (float('inf'))
dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]
res = INF

for j in range(M):
    for k in range(3):
        dp[0][j][k] = matrix[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 0) or (j == M - 1 and k == 2):
                dp[i][j][k] = INF
                continue
            if k == 0:
                dp[i][j][k] = matrix[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            elif k == 1:
                dp[i][j][k] = matrix[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            else:
                dp[i][j][k] = matrix[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])


for j in range(M):
    res = min(res, min(dp[-1][j]))
    
print(res)