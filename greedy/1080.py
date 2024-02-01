import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
B = [list(map(int, list(input().rstrip()))) for _ in range(N)]
cnt = 0


def rev(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if not A[i][j]:
                A[i][j] = 1
            else:
                A[i][j] = 0


if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                rev(i, j)
                cnt += 1

if cnt != -1 and A != B:
    cnt = -1

print(cnt)