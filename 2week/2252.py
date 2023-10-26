import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
indegree = [0] * (N + 1)
data = [[] for x in range(N+1)]

# 위상정렬로 간다
for _ in range(M):
    start,end = map(int,sys.stdin.readline().split())
    data[start].append((end))
    indegree[end] += 1

def topol():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in data[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
    for i in result:
        print(i, end=' ')

topol()