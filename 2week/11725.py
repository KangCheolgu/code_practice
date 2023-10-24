from collections import deque
from heapq import heappush, heappop
import sys
node = int(sys.stdin.readline())

graph = [[] for _ in range(node+1)]
        



while True:
    try:
            a,b = map(int,sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
    except:
        break

# 거리가 2인걸 어떻게 찾느냐
# 없으면 -1을 어떻게 출력하느냐

ans = []

def bfs(graph, start):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (node+1)
    visited[start] = True
    while queue:
        # parent 는 부모노드
        v, parent = queue.popleft()

        # print('v',v,'parent',parent)

        if parent != 0 :
            heappush(ans,(v,parent))

        for k in graph[v]:
            if not visited[k]:
                queue.append((k,v))
                visited[k] = True


bfs(graph,1)
for i in range(len(ans)):
     print(heappop(ans)[1])