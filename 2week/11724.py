# import sys, copy
# node_count, edge_count = map(int,sys.stdin.readline().split())
# data = [list(map(int,sys.stdin.readline().split())) for x in range(edge_count)]

##################################################
# print(data)
# # 없으면 배열을 어팬드 있으면 배열을 더하기
# # start 가 1이라고 가정
# def checking():
#     tmp = []
#     for x in data:
#         isit = True
#         # tmp 안에 x 가 있나

#         if not tmp:
#             tmp.append(x)
#             continue
#         # y값을 저장해서 x가 양쪽에 하나씩 있는 경우 두개를 병합하는 조건을 짜야함
#         # 일단 배열로 해봄
#         istwo = []
#         for y in range(len(tmp)):
#             for z in range(len(tmp[y])):
#                 if tmp[y][z] == x[0] or tmp[y][z] == x[1]:
#                     tmp[y] = list(set(tmp[y]+x))
#                     istwo.append(y)
#                     print('이스투',istwo)
#                     isit = False
#                     break

#         if len(istwo) == 2:
#             tmp[istwo[0]] = list(set(tmp[istwo[0]]+tmp[istwo[1]]))
#             tmp.remove(tmp[istwo[1]])
#         elif isit == True:
#             tmp.append(x)
            
#     return tmp

# print(len(checking()))

################################### 시간초과 

# 아니면 너비 우선 탐색을 해보자 너비 우선 탐색을 돌리고 나온 루트의 갯수로 하는게 더 나아보이긴함

import sys
from heapq import heappop, heappush
from collections import deque

node_count, edge_count = map(int,sys.stdin.readline().split())
visited2= [False]*(node_count+1)

graph = [[] for _ in range(node_count+1)]

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

        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True
cnt = 0

for i in range(1, node_count+1):
    if not visited2[i]:
        bfs(graph,i,visited2)
        cnt += 1

print(cnt)
