# input = int(input())

pos = [0] * 4
flag = [False] * 4

def n_queen_put() -> None:
    for i in range(4):
        print(f'{pos[i]:2}', end='')
    print()
    
def n_queen_set(i:int) -> None:
    for j in range(4):
        if flag[j] == False:
            pos[i] = j

            if i == 3:
                n_queen_put()
            else:
                flag[j] = True
                n_queen_set(i + 1)
                flag[j] = False

        
n_queen_set(0)