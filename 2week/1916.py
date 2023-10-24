# from collections import deque
# from heapq import heappush, heappop
import sys

city = int(sys.stdin.readline())
bus = int(sys.stdin.readline())

data = [[] for _ in range(city+1)]

for _ in range(bus):
    start,end,pay = map(int,sys.stdin.readline().split())
    data[start].append((end,pay))

origin, destination = map(int, sys.stdin.readline().split())
# total_pay = None

# def dfs(_now, _value, _destination):
#     global total_pay
        
#     if _now == _destination:
#         if total_pay == None:
#             total_pay = _value
#         elif total_pay > _value:
#             total_pay = _value
#         return

#     for x in data[_now]:
#         if not visited[x[0]]:
#             visited[x[0]] = 1
#             if total_pay != None and total_pay > _value+x[1]:
#                 dfs( x[0], _value+x[1], _destination)
#             visited[x[0]] = 0


# visited = [0] * (city+1)

# visited[origin] = 1
# dfs(origin, 0, destination)
# visited[origin] = 0

# print(total_pay)

# ####################### 시간초과
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq  # 우선순위 큐 구현을 위함

# def dijkstra(data, origin):
#   distances = {node: float('inf') for node in data}  # start로 부터의 거리 값을 저장하기 위함
#   distances[origin] = 0  # 시작 값은 0이어야 함
#   queue = []
#   heapq.heappush(queue, [distances[origin], origin])  # 시작 노드부터 탐색 시작 하기 위함.

#   while queue:  # queue에 남아 있는 노드가 없으면 끝
#     current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

#     if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#       continue
    
#     for new_destination, new_distance in graph[current_destination].items():
#       distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
#       if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
#         distances[new_destination] = distance
#         heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
#   return distances

def dijkstra(_data, start,destination):
    total_pay = [None] * (city+1)  # start로 부터의 거리 값을 저장하기 위함
    total_pay[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [total_pay[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if total_pay[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        
        for new_destination, new_distance in _data[current_destination]:
            pay = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리

            if total_pay[new_destination] == None or pay < total_pay[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                total_pay[new_destination] = pay
                heapq.heappush(queue, [pay, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        
    return total_pay[destination]

print(dijkstra(data,origin,destination))



