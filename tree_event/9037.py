import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    C = [*map(int, input().split())]
    while True:
        C = [i if i % 2 == 0 else i + 1 for i in C]
        if len(set(C)) == 1:
            print(cnt)
            break
        C = [C[i]//2 + C[(i+1)%n]//2 for i in range(n)]
        cnt += 1