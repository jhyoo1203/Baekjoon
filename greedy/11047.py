n, k = map(int, input().split())
coin_list = list()
count = 0
for i in range(n):
    coin_list.append(int(input()))

for i in reversed(range(n)):
    count += k//coin_list[i]
    k = k%coin_list[i]

print(count)