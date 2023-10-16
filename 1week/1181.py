import sys
T = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for p in range(T)]

result = list(set(data))

s_data = sorted(result, key=lambda x : (len(x), x))

for i in s_data:
    print(i)
