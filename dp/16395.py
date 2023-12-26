import sys

input = sys.stdin.readline

n, k = map(int, input().split())
res = [[] for _ in range(n)]

for i in range(0, n):
    for j in range(0, i + 1):
        if i == 0 or j == 0 or j == i:
            res[i].append(1)
        else:
            res[i].append(res[i - 1][j - 1] + res[i - 1][j])

print(res[n - 1][k - 1])
