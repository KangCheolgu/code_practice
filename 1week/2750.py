import sys
T = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for p in range(T)]

data.sort()

for i in data:
    print(i)
