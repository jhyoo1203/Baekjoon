import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in input().split()])

ans = int(sys.maxsize)
glevel = 0

for i in range(257):
    use = 0
    take = 0
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                take += block[x][y] - i
            else:
                use += i - block[x][y]

    if use > take + B:
        continue

    count = take * 2 + use

    if count <= ans:
        ans = count
        glevel = i

print(ans, glevel)
