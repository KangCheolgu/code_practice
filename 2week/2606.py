import sys
from heapq import heappop, heappush
from collections import deque

node_count = int(sys.stdin.readline())
edge_count = int(sys.stdin.readline())
visited2= [False]*(node_count+1)

graph = [[] for _ in range(node_count+1)]
ans = []
for i in range(edge_count):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        ans.append(v)
        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True

bfs(graph,1,visited2)
print(len(ans)-1)