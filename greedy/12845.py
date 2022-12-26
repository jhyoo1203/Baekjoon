import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
result = 0

for i in range(n):
    if i <= 1:
        result += l[i]
    else:
        result += l[0] + l[i]

print(result)
