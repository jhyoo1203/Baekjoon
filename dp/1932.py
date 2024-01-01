import sys

input = sys.stdin.readline

n = int(input())
triangle = list()
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
        else:
            triangle[i][j] = (
                max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
            )

print(max(triangle[n - 1]))
