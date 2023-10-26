import sys
from collections import deque

# 세로크기 N 가로 크기 M
N, M = map(int,sys.stdin.readline().split())
floor_data = [list(sys.stdin.readline().rstrip())for j in range(N)]
visited = [[False] * (M) for x in range(N)]
borad_cnt = 0
print(N,M)
print(floor_data)

# 시작은 0 0 으로 시작하자

def bfs(start):
    
    queue = deque()
    queue.append(start)
    
    visited[start[1]][start[0]] = True
   
    while queue:

        # 좌표 추출
        x, y = queue.popleft()

        print('기준 장판의 위치', y+1,'y번째줄', x+1,'x번')

        if floor_data[y][x] == "-":

            nx = x + 1
            
            if  0 <= nx < M and floor_data[y][nx] == '-':
                print('확인 장판의 위치', y+1,'번째줄', nx+1,'번')
                visited[y][nx] = True
                queue.append((nx, y))

        if floor_data[y][x] == "|":
            
            ny = y + 1

            if  0 <= ny < N and floor_data[ny][x] == '|':
                print('확인 장판의 위치', ny+1,'번째줄', x+1,'번')
                visited[ny][x] = True
                queue.append((x, ny))

# 위에서 아래로, 왼쪽에서 오른쪽으로 기준으로 감 마이너스 -1 은 확인해줄 필요가 없다
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            borad_cnt += 1
            bfs((j,i))

print(borad_cnt)

        