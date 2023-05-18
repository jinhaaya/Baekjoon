import sys
import math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
area = float(0)

if d >= r1 + r2 : area = 0
elif abs(r2-r1) >= d :
    area = min(r1, r2) * min(r1, r2) * math.pi
else :
    alpha = math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
    beta = math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
    area = r1 ** 2 * alpha + r2 ** 2 * beta - d * r1 * math.sin(alpha)
 

print("%.3f" % area)