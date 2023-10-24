import sys
import heapq  # 우선순위 큐 구현을 위함

N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip())) for x in range(N)]


# def dijkstra(_data, start,destination):
#     total_pay = [None] * (city+1)  # start로 부터의 거리 값을 저장하기 위함
#     total_pay[start] = 0  # 시작 값은 0이어야 함
#     queue = []
#     heapq.heappush(queue, [total_pay[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

#     while queue:  # queue에 남아 있는 노드가 없으면 끝
#         current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

#         if total_pay[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#             continue
        
#         for new_destination, new_distance in _data[current_destination]:
#             pay = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리

#             if total_pay[new_destination] == None or pay < total_pay[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
#                 total_pay[new_destination] = pay
#                 heapq.heappush(queue, [pay, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        
#     return total_pay[destination]

# print(dijkstra(data,origin,destination))

import sys
from collections import deque


dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(row,column):
    
    queue = deque()
    queue.append((row,column))

    while queue:
        row, column = queue.popleft()
        print("'",row,",",column,"'")
        
        for i in range(4):
            nx = row + dx[i]
            ny = column + dy[i]
            print(row,'행',column,'열','확인하는 nx ny',nx,ny,'borad',board[nx][ny])
            if  0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1 :
                queue.append((nx, ny))
                board[nx][ny] = board[row][column] + 1
                    
print(bfs(0,0))