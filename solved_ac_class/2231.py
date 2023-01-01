import sys
input = sys.stdin.readline

n = int(input())
res = 0

for i in range(1, n+1):
    lst = list(map(int, str(i)))
    res = i + sum(lst)
    if res == n:
        print(i)
        break
    if i==n:
        print(0)