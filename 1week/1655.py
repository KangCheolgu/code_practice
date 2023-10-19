import sys
from queue import PriorityQueue


T = int(input())
data = [int(sys.stdin.readline()) for x in range(T)]
less_que = PriorityQueue()
more_que = PriorityQueue()
l_cnt=0
m_cnt=0

for i in data:
    
    if l_cnt == 0 and m_cnt == 0:
        less_que.put((-i,i))
        print(less_que.get())
        print(less_que._get())
        print(less_que)
        l_cnt += 1
        continue
    
    if l_cnt > m_cnt:
        # l 카운트가 더 크면 비교하여
        tmp = less_que.get()
        if tmp[1] <= i:
            less_que.put(tmp)
            more_que.put((i,i))
            m_cnt += 1
        else:
            # i 가 더 작을때
            more_que.put((-tmp[0],tmp[1]))
            less_que.put((-i,i))
            m_cnt += 1
    elif l_cnt == m_cnt:
        tmp = more_que.get()
        if tmp[1] >= i:
            more_que.put(tmp)
            less_que.put((-i,i))
            l_cnt += 1
        elif tmp[1] < i:
            less_que.put((-tmp[0],tmp[1]))
            more_que.put((i,i))
            l_cnt += 1



    
 