from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

print(graph)

def bfs(x, y):
    q = deque()
    cnt = 0
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))
    return cnt-1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            res = max(res, bfs(i, j))

print(res)