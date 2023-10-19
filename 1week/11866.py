import sys
num, interval = map(int,sys.stdin.readline().split())

data = list(range(1,num+1))
new_data = "<"
new_data2 = []
cursor = 0

# 커서를 하나 만들자 커서가 data의 len를 넘어 갔다면 넘어간 것만큼 0에서 다시 시작

while len(data) != 0:
        
    cursor = cursor + interval -1
    # print('현재 커서',cursor,'현재 데이터 크기',len(data))
    # print(data)

    while cursor >= len(data):
        cursor = cursor - len(data)

    new_data += str(data[cursor])
    if len(data) != 1:
        new_data += ", "
    else:
        new_data += ">"
    data.remove(data[cursor])

print(new_data)

# while len(data) != 0:
        
#     cursor = cursor + interval -1
#     print('현재 커서',cursor,'현재 데이터 크기',len(data))
#     print(data)

#     while cursor >= len(data):
#         cursor = cursor - len(data)

#     new_data2.append(data[cursor])
#     data.remove(data[cursor])

# print(new_data2)

