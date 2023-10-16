input = int(input())

pos = [0] * input
flag_a = [False] * input
flag_b = [False] * (input * 2 - 1)
flag_c = [False] * (input * 2 - 1)
count = 0

# def n_queen_put() -> None:
#     for i in range(input):
#         print(f'{pos[i]:2}', end='')
#     print()
    
def n_queen_set(i:int) -> None:
    global count
    for j in range(input):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + input-1]:
            pos[i] = j

            if i == input-1:
                # n_queen_put()
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + input-1] = True
                n_queen_set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + input-1] = False
    return count

print(n_queen_set(0))