import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
total = sum(h)
turn = total // 3

if total % 3 != 0:
    print('NO')
else:
    for apple in h:
        turn -= (apple//2)
    if turn > 0:
        print('NO')
    else:
        print('YES')
