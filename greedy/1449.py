n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
start = s[0]
end = s[0] + l
count = 1

for i in range(n):
    if start <= s[i] < end:
        continue
    else:
        start = s[i]
        end = s[i] + l
        count += 1

print(count)