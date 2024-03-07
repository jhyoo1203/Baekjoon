import sys
input = sys.stdin.readline

graph=[]
for i in range(5):
  graph.append(list(map(str, input().split())))
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def dfs(x, y, number):
  if len(number)==6:
    if number not in result:
      result.append(number)
    return

  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<0 or nx>=5 or ny<0 or ny>=5:
      continue
    else:
      dfs(nx, ny, number + graph[nx][ny])

result=[]
for i in range(5):
  for j in range(5):
    dfs(i, j, graph[i][j])
    
print(len(result))