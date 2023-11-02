import sys

N , K = map(int, sys.stdin.readline().split())

coin_list = [int(sys.stdin.readline().rstrip()) for x in range(N)]

cnt = 0
tmp = K

for x in range(len(coin_list),0,-1):
    if tmp >= coin_list[x-1]:
        # print('들어온 화폐',coin_list[x-1])
        cnt += tmp // coin_list[x-1]
        tmp = tmp % coin_list[x-1]

print(cnt)


