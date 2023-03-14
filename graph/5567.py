from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
res = 0

def bfs(v):
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v]+1


bfs(1)
for i in range(2, n+1):
    if visited[i]<4 and visited[i] != 0:
        res += 1

print(res)