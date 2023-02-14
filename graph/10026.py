from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
basic, rgm = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            basic += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            rgm += 1


print(basic, rgm)
