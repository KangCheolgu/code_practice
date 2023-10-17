import sys

def dfs(origin, now, value, cnt):
    global ans
    if cnt == T:
        if a[now][origin]:
            value += a[now][origin]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(T):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(origin, i, value + a[now][i], cnt + 1)
            visited[i] = 0


T = int(input())
a = [list(map(int, input().split()))for _ in range(T)]

ans = sys.maxsize
visited = [0] * T
for i in range(T):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)