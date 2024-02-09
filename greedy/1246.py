import sys

input = sys.stdin.readline

N, M = map(int, input().split())
li = sorted([int(input()) for _ in range(M)])

p = b = 0

for i in range(M):
    t = li[i] * ((M-i) if M-i <= N else N)
    if b < t:
        b = t
        p = li[i]
print(p, b)