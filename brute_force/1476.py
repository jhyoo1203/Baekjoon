import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
cnt = 1

while True:
    if (cnt-e)%15 == 0 and (cnt-s)%28 == 0 and (cnt-m) % 19 == 0:
        break
    cnt += 1

print(cnt)