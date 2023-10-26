import sys
from heapq import heappop, heappush  # 우선순위 큐 구현을 위함
from collections import deque
import copy

R, C = map(int,sys.stdin.readline().split())
input_map = [list(sys.stdin.readline().rstrip()) for x in range(R)]
visited = [[False] * (C) for x in range(R)]
origin_water = []
D_location = None
S_location = None

# 좌표저장
for y in range(C):
    for x in range(R):
        if input_map[x][y] == 'D':
            D_location = (x,y)
            visited[x][y] = True
        elif input_map[x][y] == 'S':
            S_location = (x,y)
            visited[x][y] = True
        elif input_map[x][y] == "*":
            origin_water.append((x,y))
            visited[x][y] = True
        elif input_map[x][y] == "X":
            visited[x][y] = True

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# print(D_location,S_location,origin_water,stone)

def bfs(S,W):
    queue_w = deque()
    for x in range(len(origin_water)):
        queue_w.append((W[x][0],W[x][1],0))

    queue_s = deque()
    queue_s.append((S[0],S[1],0))

    while queue_w:
        x_w, y_w, c_w = queue_w.popleft()
        c_w += 1

        for i in range(4):
            nx_w = x_w + dx[i]
            ny_w = y_w + dy[i]
            if  0 <= nx_w < R and 0 <= ny_w < C and input_map[nx_w][ny_w] == '.':
                # print("물찬곳",nx_w,ny_w)
                input_map[nx_w][ny_w] = c_w
                queue_w.append((nx_w, ny_w, c_w))

    while queue_s:
        x_s, y_s, c_s = queue_s.popleft()
        c_s += 1

        for i in range(4):
            nx_s = x_s + dx[i]
            ny_s = y_s + dy[i]

            if 0 <= nx_s < R and 0 <= ny_s < C:
                # print(input_map[nx_s][ny_s],nx_s,ny_s,visited[nx_s][ny_s])
                if input_map[nx_s][ny_s] == 'D':
                    return c_s
                
                elif  visited[nx_s][ny_s] != True:
                    if input_map[nx_s][ny_s] == '.':
                        visited[nx_s][ny_s] = True
                        queue_s.append((nx_s, ny_s, c_s))
                    
                    elif c_s < input_map[nx_s][ny_s]:
                        visited[nx_s][ny_s] = True
                        queue_s.append((nx_s, ny_s, c_s))

    return 'KAKTUS'

print(bfs(S_location,origin_water))

# for s in input_map:
#     print(s)
# for j in input_map2:
#     print(j)

# for y in range(C):
#      for x in range(R):
#         if input_map[x][y] == '.':
#             input_map[x][y] = 100
#         if isinstance(input_map[x][y], int) :
#             input_map[x][y] = input_map[x][y] + input_map2[x][y]

# print(input_map)
# 변환시킨 input_map에서 다익스트라를 쓰면 될듯
# visited = [[False] * (C) for x in range(R)]

# def dijkstra(start,destination):
#     queue = deque()
#     queue.append((start[0],start[1],0))
#     visited[start[0]][start[1]] = 1
#     while queue:
#         x, y, cnt = queue.popleft()
        
#         cnt += 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx == destination[0] and ny == destination[1]:
#                 print(cnt)
#                 return
#             if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 if isinstance(input_map[nx][ny], int) and input_map[nx][ny] > 0:
#                     queue.append((nx, ny, cnt))
    
#     print("KAKTUS")

# dijkstra(S_location,D_location)