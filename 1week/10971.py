import sys

T = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for p in range(T)]

routes = list()

def put_route(route:list):
    route.append(route[0])
    routes.append(route)
    
def to_destination(start:int,destination:list[int]) -> int:
    route.append(start)
    destination.remove(start)

    if len(destination) == 0:
        put_route(route)
        destination.append(start)
    else:
        for j in destination:
            to_destination(j,destination)
            destination.append(start)



for origin in range(T):
    route = list()
    destinations = list(range(T))

    to_destination(origin,destinations)