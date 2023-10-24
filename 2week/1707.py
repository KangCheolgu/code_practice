from collections import deque
from heapq import heappush, heappop
import sys

T = int(input())

# 스타트는 무조건 1, B
def bfs(graph, start:int,_node):
    queue = deque()
    queue.append((start, 1))
    visited = [False] * (_node+1)
    _color = [None]*(_node+1)
    visited[start] = True
    _color[start] = 1
    while queue:
        # color 는 색깔
        v, color = queue.popleft()

        # print('v',v,'color',color)
        connect = []

        for k in graph[v]:

            connect.append(k)

            if not visited[k]:
                visited[k] = True

                if color == 1:
                    _color[k] = 0
                    queue.append((k,0))
                else:
                    _color[k] = 1
                    queue.append((k,1))
                
                # print("k", k , '색' ,_color[k])
        
        for c in range(len(connect)):
            
            if c == 0:
                first = _color[connect[c]]

            # print('비교에 들어옴', first,'색깔',_color[connect[c]])
            if first != _color[connect[c]]:
                print('NO')
                return
        
    print('YES')




for i in range(T):
    node, edge = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node+1)]
    

    for j in range(edge):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
    bfs(graph,1,node)  
