import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h_list = list(input().rstrip())
cnt = 0

for i in range(n):
    if h_list[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if h_list[j] == 'H':
                h_list[j] = 0
                cnt += 1
                break

print(cnt)