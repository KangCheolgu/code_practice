import sys, copy
data = int(sys.stdin.readline().rstrip())
compare = copy.deepcopy(data)
cnt = 0

# while True:
#     cnt += 1
#     # print('카운트', cnt)
    
#     data = list(data)

#     if len(data) == 1:
#         data = [0,data[0]]

#     sum = int(data[0]) + int(data[1])
#     # print(data[0],"+", data[1],"=",sum)

#     sum_list = list(str(sum))
#     # print('합 리스트',sum_list)
    
#     # 더해서 더한것의 1의자리수와 data [1]을 더해서 새로운 수를 data로 만든다.

#     if len(sum_list) == 1:
#         data = data[1] + sum_list[0]
#     else:
#         data = data[1] + sum_list[1]
    
#     # print('new data', data)
#     # print('비교대상',compare)

#     if data == compare:
#         print(cnt)
#         break

while True:
    cnt += 1

    x = data//10
    y = data%10

    sum = x + y
    sum_one = sum%10

    data = y*10+sum_one

    if data == compare:
        print(cnt)
        break
    


