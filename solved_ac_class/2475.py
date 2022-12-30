list = list(map(int, input().split()))
res = 0
for i in list:
    res += i*i

print(res % 10)
