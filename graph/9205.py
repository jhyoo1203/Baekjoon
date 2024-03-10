from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print("sad")
    

t = int(input())
for i in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    fest = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    bfs()