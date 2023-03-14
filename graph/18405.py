from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append(((graph[i][j], i, j)))
S, X, Y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(X, Y):
    q = deque(virus)
    cnt = 0
    while q:
        if cnt == S:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not graph[nx][ny]:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        cnt += 1
    return graph[X-1][Y-1]

virus.sort()
print(bfs(X, Y))