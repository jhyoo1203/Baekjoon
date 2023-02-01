n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        idx1 += 1
                    if board[a][b] != 'W':
                        idx2 += 1
                else:
                    if board[a][b] != 'W':
                        idx1 += 1
                    if board[a][b] != 'B':
                        idx2 += 1

        result.append(idx1)
        result.append(idx2)

print(min(result))
