import sys
T = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for p in range(T)]
color = 0
blue_count = 0
white_count = 0


def checking(size:int,start_x:int,start_y:int):
    global blue_count
    global white_count
    global color
    pure = True
    print('체킹용','시작점',start_x,start_y)
    
    for i in range(start_y,size + start_y):  
        for j in range(start_x,size + start_x):
            color = data[start_y][start_x]
            print('처음 색깔',color,'나중 색깔', data[i][j],'시작점',start_x,start_y,'사이즈',size,'x y',j,i)

            if data[start_y][start_x] != data[i][j]:
                # 만약 처음것과 그 다음중 어떤 하나라도 다르다면 4등분
                print('바뀜')
                pure = False
                checking(size//2,start_x,start_y)
                checking(size//2,start_x+size//2,start_y)
                checking(size//2,start_x,start_y+size//2)
                checking(size//2,start_x+size//2,start_y+size//2)
                break

        if pure == False:
            break
        
    if pure == True and color == 1:
        blue_count += 1
        print('블루카운트 업',blue_count)
    elif pure == True and color == 0:
        white_count += 1
        print('화이트카운트 업',white_count)
        

checking(T,0,0)
print(white_count)
print(blue_count)

        




        

        
