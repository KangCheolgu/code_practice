import sys, copy

N = int(input())
apple_num = int(input())
apple_data = [list(map(int,sys.stdin.readline().split())) for x in range(apple_num)]

moving_num = int(input())
moving_data = [sys.stdin.readline().split() for x in range(moving_num)]

second = 0
snake = [[1,1]]
cursor = 0
dir_list = ['E','N','W','S']
direction = dir_list[cursor]


def command(second):
    global direction, cursor
    for x in moving_data:
        if int(x[0]) == second:
            if x[1] == 'L':
                cursor += 1
                if cursor == 4:
                    cursor = 0
                moving_data.remove(x)
                break
            elif x[1] == 'D':
                cursor -= 1
                if cursor == -1:
                    cursor = 3
                moving_data.remove(x)
                break

    direction = dir_list[cursor]


def move(direction, input_snake:list):
    tmp= []
    snake=[]
    for i in range(len(input_snake)-1):
        tmp.append(input_snake[i].copy())
    
    if direction == 'E':
        input_snake[0][1] += 1
    elif direction == 'N':
        input_snake[0][0] -= 1
    elif direction == 'W':
        input_snake[0][1] -= 1
    elif direction == 'S':
        input_snake[0][0] += 1

    snake.append(input_snake[0])

    for i in tmp:
        snake.append(i)

    print('이동 후',snake)
    return snake

def crash_check(_snake:list,b_snake:list):
    for i in range(len(b_snake)):
        # print('몸통',snake[i])
        if _snake[0] == b_snake[i]:
            print('몸과 부딪힘')
            return True

    # 벽이랑 부딪힐 경우
    if _snake[0][0] < 1 or _snake[0][1] < 1 or _snake[0][0] > N or _snake[0][1] > N:
        print('벽과 부딪힘')
        return True

def apple_check(head, trace):
    global snake
    for x in apple_data:
        if x == head:
            snake.append(trace.copy())
            print(x,"위치의 사과 먹음",trace,"위치에 꼬리생김")
            print('사과를 먹은 후 스네이크',snake)
            apple_data.remove(x)


while True:
    second += 1
    tail = snake[-1].copy()
    print(second,'초')

    before_snake = copy.deepcopy(snake)
    print('이동 전', snake)
        # 이동
    snake = move(direction, snake)
    # 이동 후 판별
    # 부딫혔나
    if crash_check(snake,before_snake) == True:
        break
    # 사과를 먹었나 먹었으면 뱀 배열 나중
    apple_check(snake[0],tail)

    # print(snake[0],len(snake), second)
    # x초가 끝난 후 다음 이동 데이터 입력
    command(second)

    

print(second)

    


