n = int(input())
s = list(map(int, input().split()))
result = 0

s.sort()

for i in range(1, n+1):
    result += sum(s[0:i])

print(result)