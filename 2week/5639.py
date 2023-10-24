# 이진 순회 반대
# 전위 순회 결과값으로 이진트리를 만들고 이를 후위순회 하라
# 전위 순회 규칙 root나 parent node 보다 작으면 왼쪽 크면 오른쪽 

import sys, copy
data = []


# while True:
#     node = sys.stdin.readline().rstrip()
#     print(node)
#     if node == "":
#         break

#     data.append(node)

while True:
    try:
        data.append(int(sys.stdin.readline().rstrip()))
    except:
        break

ans = []

def make_tree(node):
    global ans
    print('들어간 노드',node,ans)
    #  루트가 들어갈때
    if not ans:
        ans.append([node,'.','.'])
        return
    # 작으면 작은거 크면 큰거 찾아서 그것의 레프트 라이트가 비어있으면
    # 거기에 추가하면서 ans에도 추가
    node_num = 0
    parent = data[0]

    while True:
        for p in range(len(ans)):
            if ans[p][0] == parent:
                node_num = p
                
        if ans[node_num][0] > node:
            if ans[node_num][1] == '.':
                ans[node_num][1] = node
                ans.append([node,'.','.'])
                return
            else:
                parent = copy.deepcopy(ans[node_num][1])
        else:
            if ans[node_num][2] == '.':
                ans[node_num][2] = node
                ans.append([node,'.','.'])
                return
            else:
                parent = copy.deepcopy(ans[node_num][2])

for i in data:
    make_tree(i)

ans2 = []

def postorder(node:str):
    global ans2
    
    for i in range(len(ans)):
        if ans[i][0] == node:
            left = ans[i][1]
            right = ans[i][2]
            break


    if left != '.':
        # str 을 반환하니 찾아야 하나? 
        postorder(left)

    if right != '.':
        postorder(right)
    
    print(node)

postorder(ans[0][0])

            