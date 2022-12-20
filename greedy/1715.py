import sys
import heapq

n = int(sys.stdin.readline())
cs = []
for _ in range(n):
    heapq.heappush(cs, int(sys.stdin.readline()))

if len(cs) == 1:
    print(0)
else:
    result = 0
    while len(cs) > 1:
        temp1 = heapq.heappop(cs)
        temp2 = heapq.heappop(cs)
        result += temp1 + temp2
        heapq.heappush(cs, temp1 + temp2)
    print(result)