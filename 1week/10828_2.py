import sys
T = int(input())
data = []

for i in range(T):
    command = sys.stdin.readline().split()
    # print('command',i,command[i][0])

    if command[0] == 'push':
        data.append(command[1])
    
    elif command[0] == 'pop':
        if len(data) != 0:
            print(data.pop())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(data))

    elif command[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(data) == 0 :
            print(-1)
        else:
            print(data[-1])
    
    # print('현재 데이터', data)

