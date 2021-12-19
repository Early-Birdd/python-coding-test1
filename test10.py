#DFS/BFS 3번

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(i,j):
    #0,0 부터 시작
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        dfs(i + 1, j)
        return True
    else:
        return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)