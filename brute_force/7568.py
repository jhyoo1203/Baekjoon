import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    x, y = map(int, input().split())
    list.append([x, y])

for i in list:
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')