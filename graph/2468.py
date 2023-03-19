from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
maxNum = 0
res = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(h, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]>h and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


for height in range(100):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j]>height and not visited[i][j]:
                bfs(height, i, j)
                cnt += 1
    if res < cnt:
        res = cnt

print(res)