import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
data_list = [list(map(int,sys.stdin.readline().split())) for x in range(N)]

dp = [[0]* (N+1) for x in range(N+1)]
tmp_list = deque()
# 먼저 두개를 곱하자

# 디피 초기값

for i in range(1,len(data_list)):
    dp[i][i+1] = data_list[i-1][0] * data_list[i-1][1] * data_list[i][1]
    tmp_list.append((data_list[i-1][0], data_list[i][1], dp[i][i+1]))



for j in range(1,len(data_list)):
    for i in range(1,len(data_list)):
        dp[i][j+i]
        if i-1 > 0 and i+j+1 < len(data_list):
            x , y = tmp_list.popleft()
            dp[i-1][j+i] = dp[i][j+i] + data_list[i-2][0] * x * y
            tmp_list.append((data_list[i-1][0],data_list[i][1]))

        print(data_list)
        tmp_0,tmp_1 = tmp_list.popleft()
        
        dp[i+1][j+i] = 


for x in dp:
    print(x)       