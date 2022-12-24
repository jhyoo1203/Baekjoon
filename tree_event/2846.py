n = int(input())
p = list(map(int, input().split()))
temp = 0
result = []

for i in range(1, n):
    if p[i] > p[i-1]:
        temp += p[i]-p[i-1]
        if i == n-1:
            result.append(temp)
    else:
        result.append(temp)
        temp = 0

print(max(result))