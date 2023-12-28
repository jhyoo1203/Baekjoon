import sys

input = sys.stdin.readline

N = int(input())

costList = [0] * 1001
jinju_charge = 0
cnt = 0

for _ in range(N):
    d, c = map(str, input().split())
    cost = int(c)

    if d == "jinju":
        jinju_charge = cost
    elif cost > 1000:
        cnt += 1
    else:
        costList[cost] += 1

for i in range(jinju_charge + 1, 1001):
    cnt += costList[i]

print(jinju_charge)
print(cnt)
