def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

x1, y1, x2, y2 = (list(map(int, input().split())))
x3, y3, x4, y4 = (list(map(int, input().split())))
if ccw(x1, y1, x2, y2, x3, y3)==ccw(x1, y1, x2, y2, x4, y4)==ccw(x3, y3, x4, y4, x1, y1)==ccw(x3, y3, x4, y4, x2, y2)==0 :
    if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y1 >= min(y3, y4) and y1 <= max(y3, y4) : print(1)
    elif x2 >= min(x3, x4) and x2 <= max(x3, x4) and y2 >= min(y3, y4) and y2 <= max(y3, y4) : print(1)
    elif x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2) : print(1)
    elif x4 >= min(x1, x2) and x4 <= max(x1, x2) and y4 >= min(y1, y2) and y4 <= max(y1, y2) : print(1)
    else : print(0)
elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0: print(1)
else : print(0)