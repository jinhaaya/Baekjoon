import sys
sys.setrecursionlimit(10000)

def distance(p1, p2) :
    dx = p2[0] - p1[0]
    if dx < 0 : dx = -dx
    dy = p2[1] - p1[1]
    if dy < 0 : dy = -dy
    return dx+dy





N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
car1 = [1,1]
car2 = [N,N]
cases = []
for _ in range(W): cases.append(list(map(int, sys.stdin.readline().split())))


##2618