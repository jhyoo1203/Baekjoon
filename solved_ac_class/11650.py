import sys
input = sys.stdin.readline

n = int(input())
i = []
for _ in range(n):
    x, y = map(int, input().split())
    i.append([x, y])

i.sort(key=lambda x: (x[0], x[1]))

for idx in i:
    print(idx[0], idx[1])