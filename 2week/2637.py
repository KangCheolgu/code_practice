import sys
from collections import deque

# 완제품 N
N = int(sys.stdin.readline().rstrip()) 
M = int(sys.stdin.readline().rstrip())
indegree = [0] * (N + 1)
data = [[] for x in range(N+1)]
ans = []
basic_parts = []

for _ in range(M):
    start,end,time = map(int,sys.stdin.readline().split())
    data[end].append((end,start,time))
    indegree[start] += 1

def topol():
    global basic_parts
    global ans
    
    queue = deque() # 큐 기능을 위한 deque 라이브러리 사용

    for i in range(1, N + 1):
        if indegree[i] == 0:
            basic_parts.append(i)
            for j in range(len(data[i])):
                queue.append(data[i][j])

    ans = [[0 for i in range(M)] for j in range(len(basic_parts)+1)]
    
    while queue:
        print(queue)
        now, target, time = queue.popleft()

        if now in basic_parts:
            ans[now][target] += time
        else:
            for x in range(1,len(basic_parts)+1):
                if ans[x][now] != 0:
                    ans[x][target] += ans[x][now]*time
       
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        indegree[target] -= 1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[target] == 0:
            for x in data[target]:
                queue.append(x)

topol()

for x in basic_parts:
    print(x, ans[x][7])
