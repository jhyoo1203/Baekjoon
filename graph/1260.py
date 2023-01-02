from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs_visited = [False]*(n+1)
bfs_visited = [False]*(n+1)


def dfs(V):
    dfs_visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(V):
    q = deque([V])
    bfs_visited[V] = True
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in graph[V]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = True


dfs(v)
print()
bfs(v)
