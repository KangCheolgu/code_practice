import sys
from heapq import heappop, heappush
from collections import deque

node_count, edge_count, root = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for x in range(edge_count)]
visited = [False]*(node_count+1)

# 루트값을 첫항으로 가지는 데이터를 찾고 그 데이터의 도착지를 heapq에 넣는다.
# 출발지는 visited를 True 시킨다.
# heappop을 하여 도착지를 추출한 다음 그 도착지를 출발지로 하는 어 양방향이네
cnt = 0
ans1 = []
ans2 = []
visited = [False]*(node_count+1)
visited2= [False]*(node_count+1)

def dfs(_root):
    tmp = []
    visited[_root] = True
    print(_root, end=" ")
    for x in data:
            if x[0] == _root:
                heappush(tmp,x[1])
            elif x[1] == _root:
                heappush(tmp,x[0])

    for i in tmp:
        if not visited[i]:
            dfs(i)
    
def bfs(_root):
    tmp2 = []
    queue = deque([_root])
    visited2[_root] = True
    while queue:
        v = queue.popleft()

        for x in data:
            if x[0] == v:
                heappush(tmp2,x[1])
            elif x[1] == v:
                heappush(tmp2,x[0])

        
        print(v, end=" ")
        for i in tmp2:
            if not visited2[i]:
                visited2[i] = True
                queue.append(i)


dfs(root)
print()
bfs(root)
