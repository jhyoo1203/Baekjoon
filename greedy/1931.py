n = int(input())
time = []
count = 0
last = 0
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time)
time = sorted(time, key=lambda a: a[1])

for i, j in time:
    if i >= last:
        count += 1
        last = j

print(count)