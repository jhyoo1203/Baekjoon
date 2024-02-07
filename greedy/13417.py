from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    card = input().split()
    q = deque()
    q.append(card[0])
    start = card[0]

    for i in range(1, N):
        if start >= card[i]:
            q.appendleft(card[i])
            start = card[i]
        else:
            q.append(card[i])
    
    print(''.join(q))