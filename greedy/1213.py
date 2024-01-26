import sys

input = sys.stdin.readline

name = list(input().rstrip())

ans = ""
tmp = ""

cnt = [0 for _ in range(26)]
odd = 0
for i in name:
    cnt[ord(i) - 65] += 1

for i in range(26):
    if cnt[i] % 2 == 1:
        odd += 1
        tmp = chr(i + 65)
    ans += chr(i + 65) * (cnt[i] // 2)

reverse = list(ans)
reverse.reverse()
ans += tmp + "".join(map(str, reverse))

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(ans)
