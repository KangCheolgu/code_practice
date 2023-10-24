import sys
from heapq import heappop, heappush

node_count, edge_count = map(int,sys.stdin.readline().split())
# data = [list(map(int,sys.stdin.readline().split())) for x in range(edge_count)]

########################### Kruskal 알고리즘

# node_data = [i for i in range(node_count+1)]

# data.sort(key=lambda x : x[2])

# print('가중치 오름차순 으로 정렬된 데이터',data)

# def check(x):
#     if x != node_data[x]:
#         node_data = check(node_data[x])
#     return node_data[x]

# answer = 0
# for start, end, v in data:
#     sRoot = check(start)
#     eRoot = check(end)
#     if sRoot != eRoot:
#         if sRoot > eRoot:
#             node_data[sRoot] = eRoot
#         else:
#             node_data[eRoot] = sRoot
#         answer += v
 
# print(answer)

###########################################

# 내가 생각한 매커니즘은 prim 알고리즘과 비슷하다
############################ Prim 알고리즘

# import sys
# import heapq
# input = sys.stdin.readline
 
# V, E = map(int, input().split())
# visited = [False]*(V+1)
# Elist = [[] for _ in range(V+1)]
# heap = [[0, 1]]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     Elist[s].append([w, e])
#     Elist[e].append([w, s])
 
# answer = 0
# cnt = 0
# while heap:
#     if cnt == V:
#         break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         visited[s] = True
#         answer += w
#         cnt += 1
#         for i in Elist[s]:
#             heapq.heappush(heap, i)
 
# print(answer)

# ########################################

visited = [False]*(node_count+1)
data = [[] for _ in range(node_count + 1)]

for _ in range(edge_count):
    s,e,v = map(int, sys.stdin.readline().split())
    data[s].append([v,e])
    data[e].append([v,s])

# 힙구조는 가장 앞에가 우선순위가 제일 높은걸 자동으로 sort해서 넣어줌
# 그 다음게 2번째 우선순위라고는 장담못함

def prim(start, value):

    tmp = [[value,start]]
    total = 0
    cnt = 0

    while cnt < node_count:

        k, v = heappop(tmp)

        if visited[v]: 
            continue

        visited[v] = True
        total += k
        cnt += 1

        for x,y in data[v]:
            heappush(tmp,[x,y])
    return total

print(prim(1,0))

