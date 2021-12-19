#DFS(스택, 재귀)/BFS(큐) 2-1

# def dfs(graph, v, visited):
#     visited[v] = True
#     #줄 바꿈 없음
#     print(v, end = ' ')
#     for i in graph[v]:
#         if visited[i] == False:
#             dfs(graph, i, visited)
#
# graph = [
#     #노드는 1부터 시작이므로 0은 비움
#     [],
#     #차례대로 인접 노드 작성
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
#8번 노드까지니까 8 + 1
# visited = [False] * 9
#
# dfs(graph, 1, visited)

#DFS/BFS 2-2

from collections import deque

def bfs(graph, x, visited):
    #시작노드 삽입
    queue = deque([x])
    visited[x] = True

    #큐가 빌 때까지 반복
    while queue:
        y = queue.popleft()
        print(y, end = ' ')
        for i in graph[y]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)