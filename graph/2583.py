from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            res.append(bfs(i, j))

res.sort()
print(len(res))
for i in res:
    print(i, end=' ')
