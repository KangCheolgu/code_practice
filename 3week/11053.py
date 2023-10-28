# import sys
# from collections import deque

# T = int(sys.stdin.readline().rstrip())

# num_list = list(map(int, sys.stdin.readline().split()))
# queue = deque()

# for x in num_list:
#     queue.append(x)

# longest = 0

# while queue:
#     compare = 0
#     dp = [0] * (len(queue)+1)
#     for i in range(len(queue)):
#         if queue[i] > compare:
#             dp[i+1] = dp[i] + 1
#             compare = queue[i]
#         else:
#             dp[i+1] = dp[i]

#     if dp[len(queue)] > longest:
#         longest = dp[len(queue)]

#     queue.popleft()


# cnt = 0
# while queue:
#     compare = 0
#     cnt = 0
#     for i in range(0,len(queue)):
#         if queue[i] > compare:
#             cnt += 1
#             compare = queue[i]

#     if cnt > longest:
#         longest = cnt
        
#     queue.popleft()

# print(longest)

import sys

T = int(sys.stdin.readline().rstrip())

num_list = list(map(int, sys.stdin.readline().split()))
# 각 원소에서 시작하는 증가 수열의 길이를 저장

dp = [1] * T  

for i in range(T):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열 중 최댓값을 찾아 가장 긴 증가하는 부분 수열의 길이로 사용
longest = max(dp)

print(longest)