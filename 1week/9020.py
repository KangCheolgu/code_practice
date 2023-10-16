import sys

T = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for p in range(T)]

for k in data:
    
    num = int(k/2)
    
    for j in range(1,num):

        prime = False
        prime2 = False
 
        tmp = num - j

        for i in range(2,tmp):

            if i == tmp-1:
                if tmp % i == 0:
                    break
                else:
                    prime = True
                    break
            
            if tmp % i == 0:
                break
       
        if prime == True:
            tmp2 = k - tmp
            
            for b in range(2,tmp2):

                if tmp2 % b == 0:
                    break
          
                if b == tmp-1:
                    if tmp2 % b == 0:
                        break
                    else:
                        prime2 = True
                        break

        if prime == True and prime2 == True:
            print(tmp,k-tmp)
            break
    
    if num == 1:
        print("1 1")
        continue
    elif num == 2:
        print("2 2")
        continue
    elif num == 3:
        print("3 3")
        continue