from collections import deque
from heapq import heappush, heappop
import copy
import sys
node = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

plus,minus,time,divide = map(int,sys.stdin.readline().split())
operation_list = []

for i in range(plus):
    operation_list.append(0)
for j in range(minus):
    operation_list.append(1)
for k in range(time):
    operation_list.append(2)
for l in range(divide):
    operation_list.append(3)

visited = [False] * (node)  
min = None
max = None 

def dfs(value, cnt):
    global min, max
    if cnt == node-1:
        print(value)
        if min == None and max == None:
            min = copy.deepcopy(value)
            max = copy.deepcopy(value)
        if min > value:
            min = copy.deepcopy(value)
        if max < value:
            max = copy.deepcopy(value)


    for i in range(node-1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            if operation_list[i] == 0:
                dfs(value + num_list[cnt], cnt)
            elif operation_list[i] == 1:
                dfs(value - num_list[cnt], cnt)
            elif operation_list[i] == 2:
                dfs(value * num_list[cnt], cnt)
            elif operation_list[i] == 3:
                if value < 0:
                    dfs(-(-value//num_list[cnt]),cnt)
                    
                else:
                    dfs(value // num_list[cnt], cnt)
            cnt -= 1
            visited[i] = 0

visited = [0] * (node-1)
print(operation_list)
dfs(num_list[0], 0)
print(max)
print(min)




