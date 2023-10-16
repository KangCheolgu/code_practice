import sys
input = int(input())

def hanoi(input : int, x : int, y : int) -> None:
        
        if input > 1:
            hanoi(input-1, x, 6-y-x)

        print(x,y)

        if input > 1:
            hanoi(input-1, 6-y-x, y)

print(2**input-1)
if input <= 20 :
    hanoi(input,1,3)
