import sys
T = int(input())
data = []
count = 0

for i in range(T):
    command = sys.stdin.readline().split()
    # print('command',i,command[0])

    if command[0] == 'push':
        data.append(command[1])
    
    elif command[0] == 'pop':
        if len(data) - count != 0:
            print(data[count])
            count += 1
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(data) - count)

    elif command[0] == 'empty':
        if len(data) - count == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(data) - count == 0 :
            print(-1)
        else:
            print(data[count])

    elif command[0] == 'back':
        if len(data) - count == 0 :
            print(-1)
        else:
            print(data[-1])
    
    print('현재 데이터', data)

