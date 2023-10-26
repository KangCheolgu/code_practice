import sys
from heapq import heappop, heappush
from collections import deque

N = int(sys.stdin.readline().rstrip())
f = [0] * (N+1)
ans1 = 0
ans2 = 0

# def fivo(number):
#     if number == 1:
#         return 1
#     elif number == 0:
#         return 0
#     else:
#         return fivo(number-1) + fivo(number-2)

# print(fivo(N))

def fivo2(number):
    f[0] = 0
    f[1] = 1
    
    for i in range(number-1):
        f[i+2] = f[i] + f[i+1]
    
    print(f[number])

fivo2(N)


