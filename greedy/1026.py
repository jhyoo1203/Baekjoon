N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
result = 0

sort_a = sorted(a_list)
sort_b = sorted(b_list, reverse=True)

for i in range(N):
    result += sort_a[i]*sort_b[i]

print(result)