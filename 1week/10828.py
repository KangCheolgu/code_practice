import sys
T = int(input())
command = [sys.stdin.readline().split() for x in range(T)]
data = []

for i in range(T):
    
    # print('command',i,command[i][0])

    if command[i][0] == 'push':
        data.append(command[i][1])
    
    elif command[i][0] == 'pop':
        if len(data) != 0:
            print(data.pop())
        else:
            print(-1)
    
    elif command[i][0] == 'size':
        print(len(data))

    elif command[i][0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)

    elif command[i][0] == 'top':
        if len(data) == 0 :
            print(-1)
        else:
            print(data[-1])
    
    # print('현재 데이터', data)

