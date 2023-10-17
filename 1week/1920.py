import sys

T = int(sys.stdin.readline())
sorted_data = sys.stdin.readline().split()
sorted_data.sort()

T2 = int(sys.stdin.readline())
data2 = sys.stdin.readline().split()

def binary_search(array, target:int, start:int, end:int):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# 타겟은 data2[i] array는 data

for i in data2:
    print(binary_search(sorted_data,i,0,T-1))
