import sys
input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))
loss.sort()
tmp = []

if n % 2 == 1:
    tmp.append(loss[-1])
    loss = loss[:-1]

for i in range(len(loss)//2):
    tmp.append(loss[i] + loss[len(loss)-1-i])

print(max(tmp))