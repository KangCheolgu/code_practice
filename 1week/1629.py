import sys

data = list(map(int,sys.stdin.readline().split()))

ans = data[0] ** data[1] % data[2]

print(ans)