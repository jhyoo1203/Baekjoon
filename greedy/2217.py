N = int(input())
w_list = []
for i in range(N):
    w_list.append(int(input()))
result = 0

w_list.sort(reverse=True)
for i in range(N):
    w_list[i] = w_list[i] * (i+1)

print(max(w_list))