import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]


def divide(x, y, n):
    color = paper[x][y]
    for row in range(x, x + n):
        for col in range(y, y + n):
            if color != paper[row][col]:
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return 0

    if color == 0:
        ans[0] += 1
    else:
        ans[1] += 1


divide(0, 0, n)
for i in ans:
    print(i)
