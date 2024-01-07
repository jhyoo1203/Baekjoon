import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(reversed(A))
increase = [1] * N
decrease = [1] * N
res = [0] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if B[i] > B[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(N):
    res[i] = increase[i] + decrease[N - i - 1] - 1

print(max(res))
