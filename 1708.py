## Convex Hull
import sys
import math

def angle(a, b) : 
    x = b[0]-a[0]
    y = b[1]-a[1]
    if x == 0 : return 90.0
    return math.degrees(math.atan(y/x))

def clockwise(a, b, c) :
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    cp = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if cp > 0 : return True
    else : return False

N = int(sys.stdin.readline())

point = []
for _ in range(N) : point.append(list(map(int, sys.stdin.readline().split())))
point.sort(key=lambda x : (x[0], x[1]))
for p in point[1:] : p.append(angle(point[0], p))
point[0].append(-90)
start = point[0]
point.sort(key=lambda x : (x[2], (start[0]-x[0])**2 + (start[1]-x[1])**2))

stack = [point[0], point[1]]
for i in range(2,len(point)) :
    while True :
        if len(stack) >= 2 and not clockwise(stack[-2][:2], stack[-1][:2], point[i][:2]) :
            stack.pop()
        else : break
    stack.append(point[i])
    
print(len(stack))