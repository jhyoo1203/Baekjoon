import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, c, p = map(int, input().split())
    cnt = 0
    
    for i in [a, b, c]:
        if i % p == 0:
            cnt += 1
    
    if cnt >= 2:
        print(1)
    else:
        print(0)