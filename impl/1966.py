from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    d = deque()
    n, m = map(int, input().split())
    importances = list(map(int, input().split()))

    for i, importance in enumerate(importances):
        d.append((i, importance))

    importances.sort()
    count = 0

    while(d):
        i, importance = d.popleft()
        
        if importance == importances[-1]:
            importances.pop()
            count += 1
            if i == m:
                print(count)
                break
        else:
            d.append((i, importance))