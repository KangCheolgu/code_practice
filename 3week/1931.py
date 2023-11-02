import sys
import heapq

N = int(sys.stdin.readline())
time_list = [list(map(int,sys.stdin.readline().split())) for x in range(N)]
queue = []
cnt = 0

for x in time_list:
    heapq.heappush(queue, (x[1], x[0]))

ans = []
while queue:
    end,start = heapq.heappop(queue)

    if len(ans) == 0:
        ans.append((start,end))
        cnt += 1
        continue

    if ans[cnt-1][1] <= start:
        ans.append((start,end))
        cnt += 1
    
print(cnt)
    


