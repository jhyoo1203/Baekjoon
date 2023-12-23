import sys

input = sys.stdin.readline

n = int(input())
road_len = list(map(int, input().split()))
oil_price = list(map(int, input().split()))


res = 0
m = oil_price[0]
for i in range(n - 1):
    if oil_price[i] < m:
        m = oil_price[i]
    res += m * road_len[i]

print(res)
