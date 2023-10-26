import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
villige_data = [list(sys.stdin.readline().rstrip()) for j in range(N)]
visited = [[False] * (N) for x in range(N)]

# 이건 상하 좌우 다 비교해야 겠네 위에서 아래, 왼쪽부터 오른쪽까지 지나가면서 쫙 훑고 0인거 무시하고 
# visited 있어야 하고, 큐 끝날때마다 +1 다음 visited가 Falue고 값이 1인것에 대해서 다시 큐에 넣고

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(start):
    cnt = 1
    queue = deque()
    queue.append(start)
    visited[start[1]][start[0]] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(y,'행',x,'열','확인하는 행렬',ny,nx)
            if  0 <= nx < N and 0 <= ny < N and villige_data[ny][nx] == '1' and visited[ny][nx] == False:
                print('조건 통과',y,'행',x,'열','확인하는 행렬',ny,nx)
                cnt += 1
                visited[ny][nx] = True
                queue.append((nx, ny))
               
    return cnt

ans = []   
villige_num = 0

for i in range(N):
    for j in range(N):
        print(visited[i][j], villige_data[i][j])
        if visited[i][j] == False and villige_data[i][j] == '1' :
            villige_num += 1
            print(i,'행', j,'열 들어감')
            ans.append(bfs((j,i)))

ans.sort()


print(villige_num)
for x in ans:
    print(x)
