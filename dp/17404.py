import sys
input = sys.stdin.readline
INF = float('inf')
R, G, B = 0, 1, 2

N = int(input())

houses = [[-1, -1, -1]]
for _ in range(N):
    houses.append(list(map(int, input().split())))

res = INF
for color in [R, G, B]:
    dp = [[-1]*3 for _ in range(N+1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = houses[1][color]

    for i in range(2, N+1):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + houses[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + houses[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + houses[i][B]
    dp[N][color] = INF
    res = min(res, min(dp[N]))
    
print(res)