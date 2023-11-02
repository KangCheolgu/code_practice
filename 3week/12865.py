import sys
N, K = map(int,sys.stdin.readline().split())

item_list = [list(map(int,sys.stdin.readline().split())) for x in range(N)]
sort_list = sorted(item_list, reverse = False)
# print(N, K, sort_list)

# dp 배열은 지니고 갈수 있는 물건의 무게
# 코인 하고 나니까 대충 어떻게 만들수 있을지 감이 잡힌다.
# 먼저 정렬을 해주면 낮은 무게의 낮은 밸류 부터 시작한다.
dp = [0] * (K+1)

for i in range(N):
    # 반복문이 돌면 dp배열의 0번을 현재 아이템 리스트의 가치의 값으로 초기화한다.
    dp[0] = sort_list[i][1]

    for j in range(K,sort_list[i][0]-1,-1):
        # print(j)
        if j == sort_list[i][0]:
            dp[j] = max(dp[j] ,dp[0])

        elif dp[j] < dp[0] + dp[j - sort_list[i][0]]:    
            dp[j] = dp[0] + dp[j - sort_list[i][0]]
    
    # print(dp)

print(dp[K])
        




