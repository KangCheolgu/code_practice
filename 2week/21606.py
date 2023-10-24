from collections import deque
from heapq import heappush, heappop
import sys
node = int(sys.stdin.readline())
node_detail = list(sys.stdin.readline().rstrip())

graph = [[] for _ in range(node+1)]
cnt = 0
print(node_detail)

for _ in range(node-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph,origin, start, visited):
    global cnt
    visited[start] = True
    print('스타트', start)
    if origin != start and node_detail[start-1] == '1':
        cnt += 1
        return
    print('오리진',origin)
    for j in graph[start]:
        if not visited[j]:
            dfs(graph, origin, j, visited)

for i in range(1,node+1):
    if node_detail[i-1] == '1':
        visited = [False] * (node+1) 
        dfs(graph,i,i,visited)

print(cnt)


