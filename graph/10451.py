import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

t = int(input())

def dfs(n):
    next = graph[n]
    
    if not visited[next]:
        visited[next] = 1
        dfs(next)
    
    return True

for k in range(t):
	n = int(input())
	graph = [0] + list(map(int, input().split()))
	visited = [0]*(n+1)
	result = 0

	for i in range(1,n+1):
		if not visited[i]:
			dfs(i)
			result += 1
	
	print(result)