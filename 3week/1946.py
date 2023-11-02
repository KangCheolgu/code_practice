import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    data_list = [list(map(int,sys.stdin.readline().split())) for x in range(N)]
    data_list.sort()
    compare = 0
    cnt = 1

    # j 는 비교군
    for j in range(1,N):
        if data_list[j][1] < data_list[compare][1]:
            compare = j
            cnt += 1

    print(cnt)
