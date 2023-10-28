import sys
T = int(sys.stdin.readline().rstrip())

for x in range(T):
    N = int(sys.stdin.readline().rstrip())
    coin_list = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline().rstrip())
    
    coin_list.sort()
    print(coin_list)
    print(target)
    dp = [0] * (target+1)
    dp[0] = 1

    for i in range(len(coin_list)):
        for j in range(coin_list[i],target+1):
            dp[j] += dp[j-coin_list[i]]

    print(dp[target])