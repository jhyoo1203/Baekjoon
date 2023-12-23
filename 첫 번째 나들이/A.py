N = int(input())
data = dict()
for i in range(N):
    d, c = input().split()
    data[d] = int(c)

cnt = 0
for charge in data:
    if data[charge] > data["jinju"]:
        cnt += 1

print(data["jinju"])
print(cnt)
