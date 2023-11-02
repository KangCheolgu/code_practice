import sys

N = int(sys.stdin.readline())

data_list = [list(map(int,sys.stdin.readline().split())) for x in range(N)]

dp = [[-1]*N for x in range(N)]

cnt = 0

# print(data_list)

# 오른쪽이나 아래쪽으로 간다. 그러면 재귀로 해볼까?
# 디피를 안써서 그런가 시간초과가 난다


def jump(x,y):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return

    jump_power = data_list[x][y]

    des_x = x + jump_power
    des_y = y + jump_power

    if jump_power > 0:
        if des_x < N:
            jump(des_x,y)
        
        if des_y < N:
            jump(x,des_y)

jump(0,0)
print(cnt)