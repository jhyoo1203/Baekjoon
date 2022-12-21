import sys
import heapq

n = int(sys.stdin.readline())
study = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    study.append([s, t])

study.sort()

room = []
heapq.heappush(room, study[0][1])

for i in range(1, n):
    if study[i][0] < room[0]:
        heapq.heappush(room, study[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, study[i][1])

print(len(room))