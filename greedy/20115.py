import sys
input = sys.stdin.readline

N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

total = drinks[-1]
for i in range(N-1):
    total += drinks[i]/2

print(total)