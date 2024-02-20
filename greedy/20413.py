import sys
input = sys.stdin.readline

n = int(input())
s, g, p, d = list(map(int, input().split()))
tear = input()
res = 0
prev = 0

for i in range(n):
    if tear[i] == 'B':
        res += s - 1 - prev
        prev = s - 1 - prev
    elif tear[i] == 'S':
        res += g - 1 - prev
        prev = g - 1 - prev
    elif tear[i] == 'G':
        res += p - 1 - prev
        prev = p - 1 - prev
    elif tear[i] == 'P':
        res += d - 1 - prev
        prev = d - 1 - prev
    elif tear[i] == 'D':
        res += d
        prev = d

print(res)