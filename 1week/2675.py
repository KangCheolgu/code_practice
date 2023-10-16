import sys

T = int(input()) #Test case
for i in range(T):
        time, strs = map(str, sys.stdin.readline().split())

        str_list = list(strs)
        tmp = ""
        for i in str_list:
            for j in range(int(time)):
                tmp += i
        
        print(tmp)
