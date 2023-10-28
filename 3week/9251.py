import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = list(sys.stdin.readline().rstrip())

# dp는 왼쪽과 위쪽을 비교하여 더 큰 값으로 초기화해주어야 하기 때문에.
# 첫줄을 0으로 채워주면 구현하기 편하다.
dp = [[0] * (len(str1) + 1) for x in range(len(str2) + 1) ] 

# 스트링 2의 첫글자와 스트링1 전체 문자와 비교
# dp는 왼쪽과 위쪽을 비교하여 더 큰 값으로 초기화해준다.
for i in range(len(str2)):
    for j in range(len(str1)):
        if str1[j] == str2[i]:
            dp[i+1][j+1] = dp[i][j] + 1

        elif dp[i+1][j] > dp[i][j+1]:
            dp[i+1][j+1] = dp[i+1][j]
        else:
            dp[i+1][j+1] = dp[i][j+1]

# for x in dp:
#     print(x)

print(dp[len(str2)][len(str1)])



