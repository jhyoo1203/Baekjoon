import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    grade = []
    for _ in range(n):
        s, m = map(int, input().split())
        grade.append([s, m])

    grade.sort()
    temp = grade[0][1]
    cnt = 1

    for j in range(n):
        if temp > grade[j][1]:
            cnt += 1
            temp = grade[j][1]

    print(cnt)