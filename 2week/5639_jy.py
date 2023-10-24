from collections import deque
import sys

sys.setrecursionlimit(10**6)

def create_travel(data):
    if not data:
        return

    now = data.popleft()
    left_subtree = deque()
    right_subtree = deque()

    while data and data[0] < now:
        left_subtree.append(data.popleft())
    while data and data[0] > now:
        right_subtree.append(data.popleft())

    create_travel(left_subtree)
    create_travel(right_subtree)
    print(now)


data = deque()

while True:
    try:
        value = int(input().rstrip())
        data.append(value)
    except:
        break

create_travel(data)