from collections import deque

N, K, M = map(int, input().split())
q = deque(range(1, N+1))

i = 0
while q:
    if i//M % 2 == 0:
        for _ in range(K-1):
            q.append(q.popleft())
    else:
        for _ in range(K):
            q.appendleft(q.pop())
    i += 1
    print(q.popleft())