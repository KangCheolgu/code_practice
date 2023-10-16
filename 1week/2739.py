import sys  
a = list(map(int,sys.stdin.readline().split(' ')))

for i in range(1,10):
    print(str(a) +" * "+ str(i) + " = " + str(a*i))