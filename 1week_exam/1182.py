import sys

T, target = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
cnt = 0
visited = [0] * T

# 그냥 전부 다 구하는게 낫겠다 외판원 문제에서 sum 추가하고 sum 을 그때 그때 확인

def sum(origin,value):
    # print('밸류',value,'타겟',target)
    global cnt
    if value == target:
        cnt += 1

    for i in range(T):
        if not visited[i] and i > origin:
            visited[i] = 1
            sum(i,value + data[i])
            visited[i] = 0

for i in range(T):
    visited[i] = 1
    # print('오리진', data[i])
    sum(i, data[i])
    visited[i] = 0

print(cnt)