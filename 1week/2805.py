import sys

# 나무의 수와 필요한 나무의 길이
tree_num, need_tree = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

def cutting(height:int, start:int, end:int):
    if start > end:
        return end
    
    mid = (start + end) // 2

    total = 0
    for i in data:
        if i >= mid:
            total += (i - mid)


    if total < height:
        return cutting(height, start, mid - 1)
    else:
        return cutting(height, mid + 1, end)

# start, end = 0 , max(data)
# while start <= end: #적절한 벌목 높이를 찾는 알고리즘
#     mid = (start+end) // 2
    
#     log = 0 #벌목된 나무 총합
#     for i in data:
#         if i >= mid:
#             log += i - mid
    
#     #벌목 높이를 이분탐색
#     if log >= need_tree:
#         start = mid + 1
#     else:
#         end = mid - 1

print(cutting(need_tree, 1, max(data)))