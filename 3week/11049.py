import sys

N = int(sys.stdin.readline().rstrip())
data_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for j in range(1, N):
    for i in range(N - j):
        dp[i][i + j] = float('inf')
        for k in range(i, i + j):
            cost = dp[i][k] + dp[k + 1][i + j] + data_list[i][0] * data_list[k][1] * data_list[i + j][1]
            dp[i][i + j] = min(dp[i][i + j], cost)

print(dp[0][N - 1])