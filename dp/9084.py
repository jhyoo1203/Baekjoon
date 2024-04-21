import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    val = int(input())
    
    dp = [0 for _ in range(val+1)]
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, val+1):
            dp[i] += dp[i-coin]
    
    print(dp[val])