from typing import MutableSequence

def q_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(pl+pr) // 2]

    a = [3,2,1,7,5,4,6]
    while pl <= pr:
        while a[pl] < x:
            pl += 1 
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
            
        # 3,2,1,6,5,4,7
    if left < pr:
        q_sort(a, left, pr)
    if pl < right:
        q_sort(a, pl, right)
        
def quick_sort(a: MutableSequence) -> None:
    q_sort(a, 0, len(a)-1)

a = [3,2,1,7,5,4,6]
b = [3,1,5,2,4]
quick_sort(b)
print(b)