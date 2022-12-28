import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))
temp = []

for i in range(1, n):
    temp.append(kids[i]-kids[i-1])

temp.sort()
print(sum(temp[:n-k]))
