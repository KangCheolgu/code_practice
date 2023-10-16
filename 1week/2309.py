import sys
data = [int(sys.stdin.readline().strip()) for p in range(9)]

total = 0
after_remove = False

for i in data:
    total += i

for j in range(8):
    for k in range(j+1, 9):
        if total - 100 == data[j] + data[k]:
            
            data.remove(data[j])
            data.remove(data[k-1])
            after_remove = True
            break

    if after_remove == True:
        data.sort()
        break


for l in data:
    print(l)


    

    