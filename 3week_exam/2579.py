import sys

N = int(sys.stdin.readline())

data_list = [int(sys.stdin.readline().rstrip()) for x in range(N)]

# print(data_list)

# 3계단 연속으로 갈수 없다. cnt를 만들어서 2이면 무조건 2칸뛰게 하자

dp = [[] for x in range(N+1)]
dp[0] = [[data_list[0], 1],[data_list[0], 2]]


# print(dp)
if N >= 2:
    dp[1] = [[data_list[1], 1],[data_list[0]+data_list[1], 2]]
    for i in range(2,N):
        for x in range(2):
            if dp[i-1][x][1] == 1:
                # print(dp[i-1][x][0],data_list[i])
                dp[i].append([dp[i-1][x][0] + data_list[i], 2])
            else:
                # print(dp[i-2][x][0], data_list[i])
                dp[i].append([max(dp[i-2][0][0], dp[i-2][1][0]) + data_list[i], 1])

print(max(dp[N-1][0][0], dp[N-1][1][0]))

