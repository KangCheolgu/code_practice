import sys  
a= int(sys.stdin.readline())

def facto(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return num * facto(num-1)


print(facto(a))