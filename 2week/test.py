import sys

T = int(sys.stdin.readline())
breaker = False
res = []


for _ in range(T):
    node, edge = map(int, sys.stdin.readline().split())
    result = [0] * (node + 1)
    #edge.sort()
    #print(edge)             #test
    edges = []
    for _ in range(edge):
        s, e = map(int, sys.stdin.readline().split())
        edges.append([s, e])
    edges.sort()
    #print(edges)                #test
    breaker = False
    set0 = set()
    set1 = set()
    colors = [-1] * (node + 1)
    for i in edges:
        s, e = i
        if s not in set0 and s not in set1:
            if e not in set0 and e not in set1:
                set0.add(s)
                set1.add(e)
            elif e in set0:
                set1.add(s)
            elif e in set1:
                set0.add(s)
        
        elif s in set0:
            if e in set0:
                breaker = True
                break
            elif e in set1:
                continue
            else:
                set1.add(e)
        elif s in set1:
            if e in set1:
                breaker = True
                break 
            elif e in set0:
                continue
            else:
                set0.add(e)
            
        #if s in set0 and e in set0:
        #    breaker = True
        #    break

        #if s in set1 and e in set1:
        #    breaker = True
        #    break
     
            
    #print(set0)             #test
    #print(set1)             #test
    #print("!!!!!!!!!!!!!!!!!!!!")           #test
    if breaker == True :
        res.append("NO")
    else: 
        res.append("YES")

for i in range(T):
    print(res[i])