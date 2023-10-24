from collections import deque
import sys
node, edge, route, start = map(int,input().split())

graph = [[] for _ in range(node+1)]
        

for i in range(edge):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[a].sort()

# 거리가 2인걸 어떻게 찾느냐
# 없으면 -1을 어떻게 출력하느냐
ans = []
def bfs(graph, start):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (node+1)
    visited[start] = True
    while queue:
        # distance 는 거리
        v, distance = queue.popleft()
        # print('v',v,'거리',distance) # 테스트용
        # 하나라도 있으면 isit 을 False로
        if distance == route:
            ans.append(v)
        elif distance > route:
            return
        # 오름차순으로 출력? 데이터 넣을때 sort해서 넣어서 괜찮음
        distance += 1
        for k in graph[v]:
            if not visited[k]:
                queue.append((k,distance))
                visited[k] = True


bfs(graph,start)
if not ans:
    print(-1)
else:
    ans.sort()
    for x in ans:
        print(x)