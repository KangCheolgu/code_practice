from collections import deque
import sys

T = int(input())



def bfs(graph, start, _node):
    queue = deque()
    queue.append((start, 1))
    _color = [None] * (_node + 1)
    visited[start] = True
    _color[start] = 1

    while queue:
        v, color = queue.popleft()
        connect = []

        for k in graph[v]:
            connect.append(k)
            if not visited[k]:
                visited[k] = True
                if color == 1:
                    _color[k] = 0
                    queue.append((k, 0))
                else:
                    _color[k] = 1
                    queue.append((k, 1))
        for c in range(len(connect)):
            if c == 0:
                first = _color[connect[c]]

            if _color[connect[c]] is not None and _color[connect[c]] != first:

                return False
            
    return True

for i in range(T):
    
    node, edge = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node + 1)]
    visited = [False] * (node + 1)
    for j in range(edge):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = True
    for k in range(1, node+1):
        if not visited[k]:
            if not bfs(graph, k, node):
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
