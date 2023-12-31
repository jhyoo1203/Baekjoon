import sys

input = sys.stdin.readline

n = int(input())
progression = list(map(int, input().split()))

for i in range(1, n):
    progression[i] = max(progression[i], progression[i] + progression[i - 1])

print(max(progression))
