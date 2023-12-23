import sys

input = sys.stdin.readline

N = int(input())

jinju_charge = None
max_charge = float("-inf")
cnt = 0

for _ in range(N):
    d, c = input().strip().split()
    current_charge = int(c)

    if d == "jinju":
        jinju_charge = current_charge
    elif current_charge > max_charge:
        max_charge = current_charge
        cnt += 1

print(jinju_charge)
print(cnt)
