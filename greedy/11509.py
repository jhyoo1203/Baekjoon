import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
cnt = [0] * 1000001

for i in h:
    if cnt[i] > 0:
        cnt[i] -= 1
        cnt[i-1] += 1
    else:
        cnt[i-1] += 1

print(sum(cnt))