import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for i in range(N)]


dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(row,column):
    
    queue = deque()
    queue.append((row,column))

    while queue:
        row, column = queue.popleft()
        
        for i in range(4):
            nx = row + dx[i]
            ny = column + dy[i]
            # print(row,'행',column,'열','확인하는 nx ny',nx,ny)
            if  0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[row][column] + 1
    
    return graph[N-1][M-1]
                
print(bfs(0,0))




# for n in range(1,N+1):
#     for m in range(1,M+1):
#         # 0일때는 확인할 필요 없지
#         if list_x[n-1][m-1] == 1:
#             # 상하좌우 다 비교 해야하네 근데 하긴 해야됨
#             graph_idx = M * (n-1) + m

#             # 왼쪽에 붙지 않으면 왼쪽과 비교
#             if m != 1:  
#                 if list_x[n-1][m-2] == 1:
#                     graph[graph_idx].append(graph_idx-1)
#                     graph[graph_idx-1].append(graph_idx)

            
#             # 위쪽에 붙지 않으면 위쪽과 비교
#             if n != 1:
#                 if list_x[n-2][m-1] == 1:
#                     graph[graph_idx].append(graph_idx - M)
#                     graph[graph_idx - M].append(graph_idx)

#             # 오른쪽에 붙지 않으면 오른쪽과 비교
#             if m != M:
#                 if list_x[n-1][m] == 1:
#                     graph[graph_idx].append(graph_idx + 1)
#                     graph[graph_idx + 1].append(graph_idx)


#             #  아래쪽에 붙지 않으면 아래쪽과 비교
#             if n != N:
#                 if list_x[n][m-1] == 1:
#                     graph[graph_idx].append(graph_idx + M)
#                     graph[graph_idx + M].append(graph_idx)

