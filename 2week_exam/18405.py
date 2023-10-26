import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
virus_data = [list(map(int, sys.stdin.readline().split())) for j in range(N)]
# S초후 X,Y에 있는 바이러스 번호
S, X, Y = map(int,sys.stdin.readline().split())
visited = [[False] * (N) for x in range(N)]
virus_state = [None] * (K+1)


dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# 좌표저장
for k in range(K):
    for y in range(N):
        for x in range(N):
            if virus_data[y][x] == k:
                virus_state[k] = (y,x)
                visited[y][x] = True

# 먼저 k 개의 바이러스들의 번호를 넣어주고, 순서대로

def bfs():
    sec_cnt = 0
    second = 0
    queue = deque()
    changed = 0
    
    # 초기값 넣어주기
    for x in range(1,len(virus_data)+1):
        if virus_state[x] != None:
            queue.append(x[0], x[1], second)

    while queue:
        x, y, s = queue.popleft()

        if sec_cnt != s:
            sec_cnt = s
            changed = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(y,'행',x,'열','확인하는 행렬',ny,nx)
            if  0 <= nx < N and 0 <= ny < N and virus_data[ny][nx] == 0 and visited[ny][nx] == False:
                print('조건 통과',y,'행',x,'열','전염된 행렬',ny,nx , s, '초')
                s += 1
                changed = 1
                visited[ny][nx] = True
                queue.append((nx, ny, s))
    
    if changed == 0:
        print(virus_data[Y][X])
        
   




