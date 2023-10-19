import sys
from queue import PriorityQueue

T = int(input())
command = [int(sys.stdin.readline()) for p in range(T)]
que = PriorityQueue()


for i in command:
    if i == 0:
        if que.empty() == True:
            print(0)
        else:
            print(que.get()[1])

    else:
        que.put((-i,i))