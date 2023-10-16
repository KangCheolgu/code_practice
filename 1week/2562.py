import sys

input_list = []
for i in range(9):
    input_list.append(int(sys.stdin.readline()))


tmp = 0
count = 1
for i in input_list:
    if tmp < i:
        tmp = i
        tmp_count = count

    count += 1
    
print(tmp)
print(tmp_count)




