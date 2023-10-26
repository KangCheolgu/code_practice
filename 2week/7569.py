import sys
from heapq import heappop, heappush  # 우선순위 큐 구현을 위함
from collections import deque

M, N, H = map(int,sys.stdin.readline().split())
box = [[list(map(int,sys.stdin.readline().split())) for i in range(N)] for j in range(H)]

dx = [-1, 1, 0, 0, 0, 0] 
dy = [ 0, 0,-1, 1, 0, 0]
dz = [ 0, 0, 0, 0,-1, 1]

def find_one(queue,cnt):
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x]  == 1:
                    queue.append((x,y,z,cnt))
    
    return

def find_zero():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x]  == 0:
                    return True
    
    return False

#  변하는게 하나도 없을때 중단후 0이 남아 있다면 -1 출력


def bfs():
    day_cnt = 0
    queue = deque()
    find_one(queue, 0)
    changed = 0
   
    while queue:

        x, y ,z, c = queue.popleft()
        
        if day_cnt != c:
            day_cnt = c
            changed = 0

        print(c,'일차')
        print('기준 토마토의 위치', z+1,'층', y+1,'번째줄', x+1,'번')

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # NX NY NZ 가 모두 범위안에 있고 토마토가 0이면 1로 바꾸고 
            if  0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0:
                print('익은 토마토의 위치', nz+1,'층', ny+1,'번째줄', nx+1,'번')
                box[nz][ny][nx] = 1
                changed = 1
                queue.append((nx, ny, nz, c+1))
                print(queue)
        
        for z in box:
            for y in z:
                print(y)
            print('--------------')
            
    if changed == 0 and find_zero() == True:
        return -1
    elif changed == 0 and find_zero() == False:
        return day_cnt
            
print(bfs())