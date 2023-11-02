import sys

string = sys.stdin.readline()
num_list = []

for x in string.split('-'):
    tmp = 0

    for y in x.split('+'):
        tmp += int(y)

    num_list.append(tmp)

ans = 0
for x in range(len(num_list)):
    if x == 0:
        ans += num_list[x]
    else :
        ans -= num_list[x]

print(ans)
