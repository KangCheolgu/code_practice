import sys
T = int(input())
data = list(map(int,sys.stdin.readline().split()))
compare = []
answer = [0 for i in range(T)]

for i in range(T):
    while compare:
        if compare[-1][1] > data[i]:
            answer[i] = compare[-1][0]+1
            break
        else:
            compare.pop()
    
    compare.append([i, data[i]])
    
print(*answer)