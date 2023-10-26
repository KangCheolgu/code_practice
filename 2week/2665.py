import sys
from heapq import heappop, heappush  # 우선순위 큐 구현을 위함
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip())) for x in range(N)]
visited = [[False] * (N) for x in range(N)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

black = deque()


def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = 1
    while heap:
        cnt, x, y = heappop(heap)
        if x == N - 1 and y == N - 1:
            print(cnt)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if board[nx][ny] == 0:
                    heappush(heap, [cnt + 1, nx, ny])
                else:
                    heappush(heap, [cnt, nx, ny])

dijkstra()


                    
                    
