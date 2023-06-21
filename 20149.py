def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def dot(dx1, dy1, dx2, dy2) :
    return dx1*dx2 + dy1*dy2

x1, y1, x2, y2 = (list(map(int, input().split())))
x3, y3, x4, y4 = (list(map(int, input().split())))
flag = 0
if ccw(x1, y1, x2, y2, x3, y3)==ccw(x1, y1, x2, y2, x4, y4)==ccw(x3, y3, x4, y4, x1, y1)==ccw(x3, y3, x4, y4, x2, y2)==0 :
    if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y1 >= min(y3, y4) and y1 <= max(y3, y4) : flag = 1
    elif x2 >= min(x3, x4) and x2 <= max(x3, x4) and y2 >= min(y3, y4) and y2 <= max(y3, y4) : flag = 1
    elif x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2) : flag = 1
    elif x4 >= min(x1, x2) and x4 <= max(x1, x2) and y4 >= min(y1, y2) and y4 <= max(y1, y2) : flag = 1
    else : flag = 0
elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0: flag = 1
else : flag = 0
print(flag)
if flag == 1 and ccw(x1, y1, x2, y2, x3, y3)==ccw(x1, y1, x2, y2, x4, y4)==ccw(x3, y3, x4, y4, x1, y1)==ccw(x3, y3, x4, y4, x2, y2)==0 :
    if x1==x3 and y1==y3 : 
        if dot(x4-x3, y4-y3, x2-x3, y2-y3) < 0 : print(x1, y1)
    elif x1==x4 and y1==y4 : 
        if dot(x3-x4, y3-y4, x2-x4, y2-y4) < 0 : print(x1, y1)
    elif x2==x3 and y2==y3 : 
        if dot(x4-x3, y4-y3, x1-x3, y1-y3) < 0 : print(x2, y2)
    elif x2==x4 and y2==y4 : 
        if dot(x3-x4, y3-y4, x1-x4, y1-y4) < 0 : print(x2, y2)

elif flag == 1 :
    print((x1*(x3*y4-x4*y3)+x2*(x4*y3-x3*y4)+x1*(x4-x3)*y2+x2*(x3-x4)*y1)/(x1*(y4-y3)+x2*(y3-y4)+(x4-x3)*y2+(x3-x4)*y1),(y2*(x1*(y4-y3)-x3*y4+x4*y3)+y1*(x3*y4+x2*(y3-y4)-x4*y3))/(x1*(y4-y3)+x2*(y3-y4)+(x4-x3)*y2+(x3-x4)*y1))
