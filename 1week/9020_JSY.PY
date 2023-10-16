import sys

T = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for p in range(T)]

def prime(num):
    if num == 2: True
    for i in range (2,num):
        if num % i == 0:
            return False
    return True

for x in data:
    even_half = x//2
    for y in range(even_half):
        tmp = even_half-y
        if prime(tmp)==True:
            tmp2 = x - tmp
            if prime(tmp2)==True:
                print(tmp,tmp2)
                break