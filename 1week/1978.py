import sys

T = int(input()) #Test case

nums = list(map(int,sys.stdin.readline().split()))
count = 0

for j in range(T): 

    for i in range(nums[j]):
        
        if nums[j] == 1 :
            break

        elif nums[j] == 2 :
            count += 1
            break
        
        if i == 0 or i == 1:
            continue

        if i == nums[j]-1 :
            if nums[j] % i == 0:
                break
            else:
                count += 1
                break
        
        if nums[j] % i == 0:
            break

print(count)

        

        

            
                

print(count)