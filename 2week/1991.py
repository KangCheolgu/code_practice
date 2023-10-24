import sys
T = int(sys.stdin.readline())
data = [list(map(str, sys.stdin.readline().split())) for i in range(T)]
# root는 무조건 data[0][0]

# 전위순회 왼쪽 우선
# 루트의 data[i][1] 우선 타고 들어감 .일때까지 -> 재귀를 해야하나?

def preorder(node:str):
    global ans
    ans.append(node)

    for i in range(T):
        if data[i][0] == node:
            left = data[i][1]
            right = data[i][2]
            break


    if left != '.':
        # str 을 반환하니 찾아야 하나? 
        preorder(left)

    if right != '.':
        preorder(right)

def inorder(node:str):
    global ans
    
    for i in range(T):
        if data[i][0] == node:
            left = data[i][1]
            right = data[i][2]
            break


    if left != '.':
        # str 을 반환하니 찾아야 하나? 
        inorder(left)

    ans.append(node)

    if right != '.':
        inorder(right)

def postorder(node:str):
    global ans
    
    for i in range(T):
        if data[i][0] == node:
            left = data[i][1]
            right = data[i][2]
            break


    if left != '.':
        # str 을 반환하니 찾아야 하나? 
        postorder(left)

    if right != '.':
        postorder(right)
    
    ans.append(node)
    
    
    


ans=[]
preorder(data[0][0])
print(*ans,sep="")
ans=[]
inorder(data[0][0])
print(*ans,sep="")
ans=[]
postorder(data[0][0])
print(*ans,sep="")





    
    
