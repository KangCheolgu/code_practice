N = int(input())
A = list(map(int,input().split()))
max_num = 1

for i in range(N-1):
    d= [1]*(N+1)
    origin = A[i]
    
    for j in range(i,N-1):

        if origin < A[j+1] :

            d[j+2] = max(d[j+2], d[j+1]+1)
            origin = A[j+1]
            if max_num < d[j+2]:
                max_num = d[j+2]
        else :
            d[j+2] = d[j+1]

print(max_num)