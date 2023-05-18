## Convex Hull
import sys
import math

def angle(a, b) : 
    x = b[0]-a[0]
    y = b[1]-a[1]
    if x == 0 : return 90.0
    return math.degrees(math.atan(y/x))

T = int(sys.stdin.readline())

for _ in range(T) :
    temp = list(map(int, sys.stdin.readline().split()))
    N = temp[0]
    point = []
    for n in range(N) :
        point.append([temp[2*n+1], temp[2*n+2], n])

    point.sort(key=lambda x : (x[0], x[1]))
    for p in point[1:] : p.append(angle(point[0], p))
    point[0].append(-90)
    start = point[0]
    point.sort(key=lambda x : (x[3], (start[0]-x[0])**2 + (start[1]-x[1])**2))

    last_angle = point[-1][3]
    reverse = []
    for i in range(N-1, 0, -1) :
        if point[i][3] == last_angle :
            reverse.append(point.pop())
        else : break
    point += reverse

    for p in point : print(p[2], end=" ")
    print("")